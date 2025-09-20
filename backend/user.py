import sqlite3

# -------------------------
# Database Setup
# -------------------------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    email TEXT NOT NULL,
    role TEXT NOT NULL
)
""")
conn.commit()

# -------------------------
# Functions
# -------------------------
def add_user(name, email, role):
    try:
        cursor.execute("INSERT INTO users (name, email, role) VALUES (?, ?, ?)", (name, email, role))
        conn.commit()
        print(f"✅ User '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print(f"❌ User '{name}' already exists!")

def show_users():
    cursor.execute("SELECT id, name, email, role FROM users")
    users = cursor.fetchall()
    print("\n📌 Current Users in System:")
    if not users:
        print("No users found.")
    else:
        for idx, user in enumerate(users, start=1):
            print(f"{idx}. Name: {user[1]}, Email: {user[2]}, Role: {user[3]}")
    print("-" * 40)

def update_user(name, new_email=None, new_role=None):
    cursor.execute("SELECT id FROM users WHERE name = ?", (name,))
    result = cursor.fetchone()
    if result:
        if new_email:
            cursor.execute("UPDATE users SET email = ? WHERE name = ?", (new_email, name))
        if new_role:
            cursor.execute("UPDATE users SET role = ? WHERE name = ?", (new_role, name))
        conn.commit()
        print(f"♻ User '{name}' updated successfully!")
    else:
        print(f"❌ User '{name}' not found!")

def delete_user(name):
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    conn.commit()
    if cursor.rowcount:
        print(f"🗑 User '{name}' deleted successfully!")
    else:
        print(f"❌ User '{name}' not found!")

def search_user(name):
    cursor.execute("SELECT id, name, email, role FROM users WHERE name = ?", (name,))
    user = cursor.fetchone()
    if user:
        print(f"🔎 Found: Name: {user[1]}, Email: {user[2]}, Role: {user[3]}")
    else:
        print(f"❌ User '{name}' not found!")

# -------------------------
# Menu System
# -------------------------
def menu():
    while True:
        print("\n===== User Management System =====")
        print("1. Add User")
        print("2. Show Users")
        print("3. Update User")
        print("4. Delete User")
        print("5. Search User")
        print("6. Exit")
        
        choice = input("👉 Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            role = input("Enter role: ")
            add_user(name, email, role)

        elif choice == "2":
            show_users()

        elif choice == "3":
            name = input("Enter name to update: ")
            new_email = input("Enter new email (leave blank if no change): ")
            new_role = input("Enter new role (leave blank if no change): ")
            update_user(name, new_email if new_email else None, new_role if new_role else None)

        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_user(name)

        elif choice == "5":
            name = input("Enter name to search: ")
            search_user(name)

        elif choice == "6":
            print("👋 Exiting program...")
            break

        else:
            print("❌ Invalid choice! Please try again.")

# -------------------------
# Run Program
# -------------------------
if __name__ == "__main__":
    menu()
    conn.close()

