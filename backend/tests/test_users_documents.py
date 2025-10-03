# backend/tests/test_users_documents.py
from backend.model.documents import WordDocument, PDFDocument, ImageDocument
from backend.model.users import User, AdminUser

def test_flow():
    user = User("pragnesh", "pragnesh@mail.com", "111111")
    admin = AdminUser("himu", "himu@mail.com", "adminpwd")

    # Create & upload (documents stored under storage/ to keep project tidy)
    word = WordDocument("storage/report.docx", "Report", "Pragnesh")
    print(user.upload_document(word, "This is the report content.\n"))

    pdf = PDFDocument("storage/ebook.pdf", "Python Guide", "Himu")
    print(user.upload_document(pdf, "PDF content - sample"))

    image = ImageDocument("storage/nature.jpg", "Nature", "Pragnesh")
    print(user.upload_document(image, ""))  # image placeholder

    # View documents
    print("User docs:", user.list_documents())

    # Read one document
    print("Read report:", word.read())

    # Admin deletes a doc
    print(admin.delete_document(user, "storage/report.docx"))

    # After delete
    print("User docs after delete:", user.list_documents())

    # Password checks
    print("Password correct?", user.check_password("111111"))
    print(admin.reset_password(user, "999999"))
    print("Password now correct?", user.check_password("999999"))

if __name__ == "__main__":
    test_flow()
