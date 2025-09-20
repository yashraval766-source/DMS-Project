import sqlite3

DB_PATH = "database/db.sqlite3"

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS documents (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()


# CREATE
def add_document(title, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO documents (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()
    return f"Document '{title}' added successfully!"


# READ
def get_document(doc_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM documents WHERE id=?", (doc_id,))
    doc = cursor.fetchone()
    conn.close()
    return doc


# UPDATE
def update_document(doc_id, new_title, new_content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE documents SET title=?, content=? WHERE id=?", (new_title, new_content, doc_id))
    conn.commit()
    conn.close()
    return f"Document {doc_id} updated successfully!"


# DELETE
def delete_document(doc_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM documents WHERE id=?", (doc_id,))
    conn.commit()
    conn.close()
    return f"Document {doc_id} deleted successfully!"


# TESTING PURPOSE
if __name__ == "__main__":
    create_table()

    print(add_document("First Doc", "This is the content of the first document."))
    print(get_document(1))

    print(update_document(1, "Updated Doc", "This is the updated content."))
    print(get_document(1))

    print(delete_document(1))
    print(get_document(1))  # should return None
