import sys, os
# project root ko path me add karna (har baar cd karne ki need nahi)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.model import Document

# Document object create
d1 = Document("demo.txt", title="Demo File", author="Pragnesh")

print("---- Document Test Start ----")

# 1. create file
d1.create("This is my first doc.")
print("File created successfully!")

# 2. read file
print("File Content (after create):")
print(d1.read())

# 3. append content
d1.append("\nExtra line added.")
print("Content appended successfully!")

# 4. read again
print("File Content (after append):")
print(d1.read())

# 5. show info
print("Document Info:")
d1.info()

# 6. delete file
d1.delete()
print("File deleted successfully!")

print("---- Document Test End ----")
