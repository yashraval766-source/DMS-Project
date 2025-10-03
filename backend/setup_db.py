from models import db
from models.member import Member
from app import app
import os

# Ensure database folder exists
database_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../database')
if not os.path.exists(database_folder):
    os.makedirs(database_folder)

# Create tables and insert first member
with app.app_context():
    db.create_all()
    print("Database and tables created successfully!")

    if Member.query.first() is None:
        test_member = Member(name="Pragnesh Raval", email="pragnesh@example.com", role="Admin")
        db.session.add(test_member)
        db.session.commit()
        print("First test member added successfully!")
    else:
        print("Members already exist in the database.")
