from document import create_table, add_document, get_document, update_document, delete_document

def menu():
    print("\n===== Document Management System =====")
    print("1. Add Document")
    print("2. View Document")
    print("3. Update Document")
    print("4. Delete Document")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    create_table()  # ensure table exists before operations

    while True:
        choice = menu()

        if choice == "1":
            title = input("Enter document title: ")
            content = input("Enter document content: ")
            print(add_document(title, content))

        elif choice == "2":
            doc_id = int(input("Enter document ID to view: "))
            doc = get_document(doc_id)
            if doc:
                print(f"\nDocument Found:\nID: {doc[0]}\nTitle: {doc[1]}\nContent: {doc[2]}")
            else:
                print("⚠️ Document not found!")

        elif choice == "3":
            doc_id = int(input("Enter document ID to update: "))
            new_title = input("Enter new title: ")
            new_content = input("Enter new content: ")
            print(update_document(doc_id, new_title, new_content))

        elif choice == "4":
            doc_id = int(input("Enter document ID to delete: "))
            print(delete_document(doc_id))

        elif choice == "5":
            print("Exiting DMS... ✅")
            break

        else:
            print("⚠️ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
