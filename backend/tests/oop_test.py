from backend.model import Document

doc = Document("demo.txt")

# Create file
doc.create("Hello, this is my first document!")

# Read file
print("File Content (after create):")
print(doc.read())

# Update file
doc.update("This is updated content.")

# Read file again
print("File Content (after update):")
print(doc.read())

# Append content
doc.append("\nThis is appended line.")

# Read file again
print("File Content (after append):")
print(doc.read())

# Delete file
doc.delete()
