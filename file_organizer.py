import os
import shutil

FILE_CATEGORIES = {
    "Images" : [".jpg", ".png", ".jpeg", ".gif"],
    "Videos" : [".mp4", ".mov"],
    "Documents" : [".pdf", ".doc", ".docx", ".txt", ".md", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Audio" : [".mp3"],
    "Archives" : [".zip", ".rar"],
    "Data" : [".csv", ".json", ".xml"],
    "Misc" : []
}

def organize_files(directory):
    """Organizes files in the given directory based on their file type"""
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        return 
    
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isdir(file_path):
            continue

        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved = True
                break

        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "Misc", filename))
    
directory_to_organize = input("Enter the directory path to organize: ")
organize_files(directory_to_organize)