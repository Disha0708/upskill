import os
import shutil

# File extensions and categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"]
}

# Ask user for folder path
folder_path = input("Enter the folder path to organize: ")

# Check if folder exists
if not os.path.exists(folder_path):
    print("❌ Folder does not exist.")
    exit()

# Organize files
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)

    if os.path.isfile(file_path):
        extension = os.path.splitext(file_name)[1].lower()
        category = "Others"

        for folder, extensions in FILE_TYPES.items():
            if extension in extensions:
                category = folder
                break

        destination_folder = os.path.join(folder_path, category)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        shutil.move(file_path, os.path.join(destination_folder, file_name))
        print(f"Moved: {file_name} → {category}")

print("\n✅ File organization completed successfully!")
