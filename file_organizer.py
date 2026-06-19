from pathlib import Path
import argparse

FILE_CATEGORIES = {
    "Images" : [".jpg", ".png", ".jpeg", ".gif"],
    "Videos" : [".mp4", ".mov"],
    "Documents" : [".pdf", ".doc", ".docx", ".txt", ".md", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio" : [".mp3"],
    "Archives" : [".zip", ".rar"],
    "Data" : [".csv", ".json", ".xml"],
    "Misc" : []
}

EXTENSION_TO_CATEGORY = {
    ext: category
    for category, extensions in FILE_CATEGORIES.items()
    for ext in extensions
}

def organize_files(directory: Path, dry_run: bool = False, recursive: bool = False) -> None:
    """Organize files in the given directory by file type."""
    if not directory.is_dir():
        print(f"Error: {directory} is not a valid directory")
        return 
 
    for category in FILE_CATEGORIES:
        (directory / category).mkdir(exist_ok=True)

    category_dirs = {directory / c for c in FILE_CATEGORIES}

    if recursive:
        paths = directory.rglob("*")
    else:
        paths = directory.iterdir()

    for path in paths:
        if not path.is_file():
            continue
        if any(parent in category_dirs for parent in path.parents):
            continue  # already organized — skip

        category = EXTENSION_TO_CATEGORY.get(path.suffix.lower(), "Misc")
        destination = directory / category / path.name

        if dry_run:
            print(f"Would move: {path.name} -> {category}/")
        else:
            path.rename(destination)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files by type.")
    parser.add_argument("directory", type=Path, help="Directory to organize")
    parser.add_argument("--dry-run", action="store_true", help="Preview without moving")
    parser.add_argument("--recursive", action="store_true", help="Include subdirectories")
    args = parser.parse_args()

    organize_files(args.directory, dry_run=args.dry_run, recursive=args.recursive)