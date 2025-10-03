# backend/Tests/test_models.py

from backend.models import Document, ProjectMember

# ----- Document Tests -----
doc1 = Document("Python", "I learn Python programming")
doc2 = Document("Geeta", "Geeta sloka")
doc3 = Document("Python", "I also learn Python")

print("----- Document Tests -----")
print(doc1)              # __str__ user-friendly
print(repr(doc1))        # __repr__ developer-friendly
print(len(doc1))         # __len__ (content length)
print(doc1 == doc3)      # __eq__ (title same)
doc4 = doc1 + doc2       # __add__ (merge documents)
print(doc4)
print(doc1 > doc2)       # __gt__ (content length comparison)
print(doc1 < doc2)       # __lt__ (content length comparison)

# ----- ProjectMember Tests -----
dev = ProjectMember("Pragnesh", "Developer")
tester = ProjectMember("Chirag", "Tester")
dev2 = ProjectMember("Raj", "Developer")

print("\n----- ProjectMember Tests -----")
print(dev)               # __str__ user-friendly
print(repr(dev))         # __repr__ developer-friendly
print(len(dev))          # __len__ (role length)
print(dev == dev2)       # __eq__ (role same)
print(dev == tester)     # False
