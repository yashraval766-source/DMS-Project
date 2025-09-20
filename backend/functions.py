documents = []   # simple in-memory database


# Add Document
def add_doc(doc_id, title, author):
    document = {
        "id": doc_id,
        "title": title,
        "author": author
    }
    documents.append(document)
    print("✅ Document added:", title)


# Display All Documents
def display_docs():
    if not documents:
        print("⚠️ No documents found.")
    else:
        print("\n📑 All Documents:")
        for doc in documents:
            print(doc)


# Delete Document
def delete_doc(doc_id):
    for doc in documents:
        if doc["id"] == doc_id:
            documents.remove(doc)
            print("🗑️ Document deleted:", doc["title"])
            return
    print("❌ Document not found!")


# Update Author
def update_author(document, new_author):
    document["author"] = new_author
    print("✏️ Author updated to:", new_author)
    return document


# Search Document by ID
def search_doc_by_id(doc_id):
    for doc in documents:
        if doc["id"] == doc_id:
            print("🔍 Document found:", doc)
            return doc
    print("❌ Document not found with ID:", doc_id)
    return None


# Search Document by Title
def search_doc_by_title(title):
    for doc in documents:
        if doc["title"].lower() == title.lower():
            print("🔍 Document found:", doc)
            return doc
    print("❌ Document not found with Title:", title)
    return None
