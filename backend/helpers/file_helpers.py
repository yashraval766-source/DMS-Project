import os
import shutil
from datetime import datetime
 
# ---------------- Basic File Helpers ----------------

def ensure_folder(folder_path: str) -> str:
    """Ensure that the given folder exists, create if not."""
    folder_path = os.path.abspath(folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
    return folder_path

def create_file(filepath: str, content: str = "") -> str:
    """Create a new file with the given content."""
    folder = os.path.dirname(filepath)
    if folder:
        ensure_folder(folder)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return f"{filepath} created successfully."

def append_to_file(filepath: str, content: str) -> str:
    """Append content to an existing file."""
    with open(filepath, "a", encoding="utf-8") as f:
        f.write("\n" + content)
    return f"Content appended to {filepath}."

def overwrite_file(filepath: str, content: str) -> str:
    """Overwrite file content with new data."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return f"{filepath} overwritten with new content."

def delete_file(filepath: str) -> str:
    """Delete a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)
        return f"{filepath} deleted successfully."
    return f"{filepath} does not exist."

def delete_folder(folderpath: str) -> str:
    """Delete a folder and all its contents."""
    if os.path.exists(folderpath):
        shutil.rmtree(folderpath)
        return f"{folderpath} and its contents deleted."
    return f"{folderpath} does not exist."

def list_files_with_sizes(folderpath: str) -> list:
    """List files in a folder with their sizes in bytes."""
    if not os.path.exists(folderpath):
        return [f"{folderpath} does not exist."]
    file_list = []
    for f in os.listdir(folderpath):
        filepath = os.path.join(folderpath, f)
        if os.path.isfile(filepath):
            size = os.path.getsize(filepath)
            file_list.append(f"{f} - {size} bytes")
    return file_list

def file_metadata(filepath: str) -> dict | str:
    """Return file metadata including size and timestamps."""
    if not os.path.exists(filepath):
        return f"{filepath} does not exist."
    stats = os.stat(filepath)
    return {
        "path": filepath,
        "size_bytes": stats.st_size,
        "last_modified": datetime.fromtimestamp(stats.st_mtime),
        "created": datetime.fromtimestamp(stats.st_ctime)
    }

# ---------------- Advanced Helpers ----------------

def backup_file(src: str, dest_folder: str = "backend/backup") -> str:
    """Create a timestamped backup of a file in the backup folder."""
    if not os.path.exists(src):
        return f"{src} does not exist."
    dest_folder = ensure_folder(dest_folder)
    base = os.path.basename(src)
    name, ext = os.path.splitext(base)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_file = os.path.join(dest_folder, f"{name}_{timestamp}{ext}")
    shutil.copy2(src, dest_file)
    return f"Backup created at {dest_file}"

def get_file_info(filepath: str) -> dict | str:
    """Return basic file info (path, size, last modified)."""
    if not os.path.exists(filepath):
        return f"{filepath} does not exist."
    size = os.path.getsize(filepath)
    mtime = os.path.getmtime(filepath)
    last_modified = datetime.fromtimestamp(mtime).strftime("%d-%m-%Y %H:%M:%S")
    return {
        "path": filepath,
        "size_bytes": size,
        "last_modified": last_modified
    }

# ---------------- File Organize Helpers ----------------

def move_file_to_archive(src_file: str, archive_folder: str = "backend/archive") -> str:
    """Move a file to the archive folder with timestamp."""
    if not os.path.exists(src_file):
        return f"{src_file} does not exist."
    archive_folder = ensure_folder(archive_folder)
    base = os.path.basename(src_file)
    name, ext = os.path.splitext(base)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_file = os.path.join(archive_folder, f"{name}_{timestamp}{ext}")
    shutil.move(src_file, dest_file)
    return f"{src_file} moved to {dest_file}"

def copy_file_to_backup(src_file: str, backup_folder: str = "backend/backup") -> str:
    """Copy a file to the backup folder with timestamp."""
    if not os.path.exists(src_file):
        return f"{src_file} does not exist."
    backup_folder = ensure_folder(backup_folder)
    base = os.path.basename(src_file)
    name, ext = os.path.splitext(base)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest_file = os.path.join(backup_folder, f"{name}_{timestamp}{ext}")
    shutil.copy2(src_file, dest_file)
    return f"{src_file} copied to {dest_file}"
