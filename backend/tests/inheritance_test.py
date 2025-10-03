from backend.model.documents import WordDocument, PDFDocument, ImageDocument

def test_documents():
    word = WordDocument("report.docx", "Project Report", "Pragnesh")
    pdf = PDFDocument("ebook.pdf", "Python Guide", "Himu")
    image = ImageDocument("nature.jpg", "Nature Image", "Pragnesh")

    print(word.open())
    print(pdf.open())
    print(image.open())

if __name__ == "__main__":
    test_documents()
