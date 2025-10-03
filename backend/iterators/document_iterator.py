from models.documents import Document

class DocumentIterator:
    def __init__(self, documents):
        self.documents = documents
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.documents):
            doc = self.documents[self.index]
            self.index += 1
            return doc
        else:
            raise StopIteration

class ReverseDocumentIterator:
    def __init__(self, documents):
        self.documents = documents
        self.index = len(documents) - 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= 0:
            doc = self.documents[self.index]
            self.index -= 1
            return doc
        else:
            raise StopIteration

class SkipDocumentIterator:
    def __init__(self, documents, step=2):
        self.documents = documents
        self.index = 0
        self.step = step

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.documents):
            doc = self.documents[self.index]
            self.index += self.step
            return doc
        else:
            raise StopIteration

class LimitedDocumentIterator:
    def __init__(self, documents, limit=2):
        self.documents = documents
        self.index = 0
        self.limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.documents) and self.index < self.limit:
            doc = self.documents[self.index]
            self.index += 1
            return doc
        else:
            raise StopIteration

class SearchDocumentIterator:
    def __init__(self, documents, keyword):
        self.documents = documents
        self.keyword = keyword
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while self.index < len(self.documents):
            doc = self.documents[self.index]
            self.index += 1
            content = doc.read()  # file content read
            if self.keyword.lower() in content.lower():
                return doc
        raise StopIteration
