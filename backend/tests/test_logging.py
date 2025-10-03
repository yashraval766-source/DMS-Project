from backend.model.documents import Document
import os

def run_tests():
    folder = "backend/files"
    os.makedirs(folder, exist_ok=True)

    doc = Document(f"{folder}/Python.txt", title="I learn Python programming", author="Pragnesh")

    print(doc.create("Hello Himu!"))
    print(doc.read())
    print(doc.append("Extra line added"))
    print(doc.update("New content"))
    print(doc.info())
    print(doc.delete())

if __name__ == "__main__":
    run_tests()
