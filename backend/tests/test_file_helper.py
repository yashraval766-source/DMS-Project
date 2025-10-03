import os
from backend.helpers import file_helpers

# Test folder aur file paths
test_folder = "backend/files/test_folder"
test_file = os.path.join(test_folder, "sample.txt")

def run_tests():
    print("\n---- Running File Helper Tests ----")

    # 1. Ensure folder
    print(file_helpers.ensure_folder(test_folder))

    # 2. Create file
    print(file_helpers.create_file(test_file, "Hello World!"))

    # 3. Append to file
    print(file_helpers.append_to_file(test_file, "This is appended content."))

    # 4. Overwrite file
    print(file_helpers.overwrite_file(test_file, "New content replaced."))

    # 5. File metadata
    print(file_helpers.file_metadata(test_file))

    # 6. List files with sizes
    print(file_helpers.list_files_with_sizes(test_folder))

    # 7. Backup file
    print(file_helpers.backup_file(test_file))

    # 8. Copy file to backup
    print(file_helpers.copy_file_to_backup(test_file))

    # 9. Move file to archive
    print(file_helpers.move_file_to_archive(test_file))

    # 10. Delete file (already moved so this checks non-existent case)
    print(file_helpers.delete_file(test_file))

    # 11. Delete folder
    print(file_helpers.delete_folder(test_folder))

    print("---- Tests Completed ----")

if __name__ == "__main__":
    run_tests()
