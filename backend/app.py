import os, webbrowser, logging
from flask import Flask, render_template, redirect, url_for, flash, request, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm, CSRFProtect
from flask_migrate import Migrate
from wtforms import StringField, PasswordField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from functools import wraps
from datetime import datetime

# ================= PATH =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'frontend', 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'frontend', 'static')
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, 'database'), exist_ok=True)
ALLOWED_EXTENSIONS = {'pdf','docx','txt','xlsx','pptx','jpg','png'}

# ================= APP =================
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.config.update(
    SECRET_KEY='thisissecretkey123',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(BASE_DIR, 'database', 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    UPLOAD_FOLDER=UPLOAD_FOLDER,
    REMEMBER_COOKIE_DURATION=86400
)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
logging.basicConfig(filename='backend.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ================= MODELS =================
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    role = db.Column(db.String(20), default='user')
    documents = db.relationship('Document', backref='uploader', lazy=True)

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tags = db.Column(db.String(200))
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    version = db.Column(db.Integer, default=1)

# ================= FORMS =================
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3,150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(3,150)])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3,150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(3,150)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('user','User'),('admin','Admin')])
    submit = SubmitField('Register')

class ResetPasswordForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3,150)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(3,150)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Reset Password')

class DocumentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    tags = StringField('Tags')
    file = FileField('File')
    submit = SubmitField('Submit')

class DummyForm(FlaskForm): pass  # CSRF token for delete

# ================= LOGIN =================
@login_manager.user_loader
def load_user(uid): return User.query.get(int(uid))

def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash('Admin access required!', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrap

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

# ================= ROUTES =================
@app.route('/')
def home(): return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            flash('Logged in successfully!', 'success')
            logging.info(f'User logged in: {user.username}')
            return redirect(url_for('home'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data).first():
            flash('Username exists', 'danger')
        else:
            hashed_pw = generate_password_hash(form.password.data)
            user = User(username=form.username.data, password=hashed_pw, role=form.role.data)
            db.session.add(user); db.session.commit()
            flash('Registration successful!', 'success')
            logging.info(f'New user: {user.username}, role: {user.role}')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logging.info(f'User logged out: {current_user.username}')
    logout_user()
    flash('Logged out successfully', 'info')
    return redirect(url_for('home'))

# ---------------- Document Helpers ----------------
def save_file(file):
    filename = secure_filename(file.filename)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(save_path):
        filename = f"{base}_{counter}{ext}"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        counter += 1
    file.save(save_path)
    return filename

# ---------------- Upload / Update ----------------
@app.route('/upload', methods=['GET','POST'])
@login_required
def upload():
    form = DocumentForm()
    if form.validate_on_submit() and form.file.data and allowed_file(form.file.data.filename):
        filename = save_file(form.file.data)
        existing_doc = Document.query.filter_by(title=form.title.data).order_by(Document.version.desc()).first()
        version = existing_doc.version+1 if existing_doc else 1
        doc = Document(title=form.title.data, filename=filename, uploader_id=current_user.id, tags=form.tags.data, version=version)
        db.session.add(doc); db.session.commit()
        flash('File uploaded successfully','success')
        logging.info(f'File uploaded: {filename} by {current_user.username}')
        return redirect(url_for('documents'))
    return render_template('upload.html', form=form)

@app.route('/documents')
@login_required
def documents():
    page = int(request.args.get('page',1))
    per_page = 5
    query = Document.query.filter_by(uploader_id=current_user.id) if current_user.role!='admin' else Document.query
    title = request.args.get('title'); tags = request.args.get('tags')
    if title: query = query.filter(Document.title.ilike(f'%{title}%'))
    if tags: query = query.filter(Document.tags.ilike(f'%{tags}%'))
    total = query.count(); docs = query.order_by(Document.upload_date.desc()).offset((page-1)*per_page).limit(per_page).all()
    return render_template('documents.html', documents=docs, page=page, total_pages=(total//per_page)+(1 if total%per_page>0 else 0), form=DummyForm())

@app.route('/download/<int:doc_id>')
@login_required
def download(doc_id):
    doc = Document.query.get_or_404(doc_id)
    if current_user.role!='admin' and current_user.id!=doc.uploader_id: flash('Permission denied!', 'danger'); return redirect(url_for('documents'))
    return send_from_directory(app.config['UPLOAD_FOLDER'], doc.filename, as_attachment=True)

@app.route('/update/<int:doc_id>', methods=['GET','POST'])
@login_required
def update_document(doc_id):
    doc = Document.query.get_or_404(doc_id)
    if current_user.role!='admin' and current_user.id!=doc.uploader_id: flash('Permission denied!', 'danger'); return redirect(url_for('documents'))
    form = DocumentForm()
    if form.validate_on_submit():
        doc.title = form.title.data; doc.tags = form.tags.data
        if form.file.data: doc.filename = save_file(form.file.data); doc.version += 1
        db.session.commit(); flash('Document updated successfully','success')
        return redirect(url_for('documents'))
    elif request.method=='GET': form.title.data = doc.title; form.tags.data = doc.tags
    return render_template('update_document.html', form=form, doc=doc)

@app.route('/delete/<int:doc_id>', methods=['POST'])
@login_required
def delete_document(doc_id):
    doc = Document.query.get_or_404(doc_id)
    if current_user.role!='admin' and current_user.id!=doc.uploader_id: flash('Permission denied','danger'); return redirect(url_for('documents'))
    try:
        path = os.path.join(app.config['UPLOAD_FOLDER'], doc.filename)
        if os.path.exists(path): os.remove(path)
        db.session.delete(doc); db.session.commit()
        flash('Document deleted successfully','success')
        logging.info(f'Document deleted: {doc.title} by {current_user.username}')
    except Exception as e: flash('Error deleting document','danger'); logging.error(f'{e}')
    return redirect(url_for('documents'))

@app.route('/reset-password', methods=['GET','POST'])
def reset_password():
    form = ResetPasswordForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if not user:
                flash('User not found', 'danger')
            else:
                user.password = generate_password_hash(form.new_password.data)
                db.session.commit()
                flash("Password reset successfully!", 'success')
                return redirect(url_for('login'))
        else:
            flash("Form validation failed", "danger")

    return render_template('reset_password.html', form=form)


@app.route('/api/documents')
@login_required
def api_documents(): return jsonify([{
    'id': d.id,'title': d.title,'filename': d.filename,'uploader_id':d.uploader_id,
    'tags':d.tags,'upload_date':d.upload_date.isoformat(),'version':d.version
} for d in Document.query.all()])

# ================= ERROR HANDLING =================
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return render_template('500.html'), 500


# ================= RUN =================
if __name__=='__main__':
    with app.app_context(): db.create_all()
    if os.environ.get('WERKZEUG_RUN_MAIN')=='true': webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=True)

