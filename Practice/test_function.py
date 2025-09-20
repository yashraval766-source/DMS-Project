import sys, os

# Backend folder ko Python path me add karna
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Backend")))

# functions.py import
from functions import add_doc, display_docs, delete_doc, update_author, documents, search_doc_by_id, search_doc_by_title


# -----------------------------
# ✅ TESTING WITH SAMPLE USERS
# -----------------------------

# Add sample documents
add_doc(1, "Python Basics", "Yash")
add_doc(2, "Functions in Python", "Parth")
add_doc(3, "OOP in Python", "Kartik")

# Display all docs
display_docs()

# Update author of 1st document
update_author(documents[0], "Rahul")

# Display again
display_docs()

# Delete document with id=2
delete_doc(2)

# Display again
display_docs()

# -----------------------------
# ✅ TESTING SEARCH FUNCTIONS
# -----------------------------
print("\n--- Testing Search Function ---")

# Search by ID
search_doc_by_id(1)      # should find Python Basics
search_doc_by_id(99)     # not found

# Search by Title
search_doc_by_title("OOP in Python")   # should find
search_doc_by_title("Java Basics")     # not found
