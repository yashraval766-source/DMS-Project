# DMS Project

## Project Overview
**DMS (Document Management System)** is a web application built using **Flask** and **SQLAlchemy**.  
It allows users to **upload, manage, and track documents** efficiently, with support for versioning and secure access.

## Features
- **User Authentication:** Register and login securely.
- **Document Upload & Download:** Users can upload documents and download them anytime.
- **Version Control:** Maintain versions of documents automatically.
- **Document Management:** Delete, archive, and search documents easily.
- **File Organization:** Uploaded files are stored in structured directories.
- **Frontend:** Clean HTML/CSS templates for a simple UI.

## Project Structure
DMS-Project/
├── Backend/ # Flask backend (routes, models, helpers)
├── Frontend/ # HTML templates & static files (CSS)
├── Database/ # SQLite database files
├── Storage/ # Uploaded documents storage
├── Migrations/ # Database migration files
├── requirements.txt # Python dependencies
└── README.md # Project documentation

bash
Copy code

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/pragneshraval288-create/DMS-Project.git
Navigate to the project folder:

bash
Copy code
cd DMS-Project
Create a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate

Linux/Mac: source venv/bin/activate

Install required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Flask app:

bash
Copy code
python app.py
Open your browser and go to: http://127.0.0.1:5000/

Future Improvements
Add role-based access control for documents.

Implement search filters for faster document retrieval.

Add automated tests (unit & integration tests).

Enhance UI/UX with a modern frontend framework (React or Bootstrap).

Optimize performance and storage for large files.

Contributing
Contributions are welcome! Please fork the repository and create a pull request.

License
This project is open-source and available under the MIT License.