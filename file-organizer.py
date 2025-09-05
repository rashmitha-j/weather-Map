import os
import shutil

# Define file categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Programs": [".py", ".c", ".cpp", ".java", ".exe"]
}

def organize_files(source_folder):
    if not os.path.exists(source_folder):
        print("❌ The source folder does not exist!")
        return

    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)

        # Skip if it’s a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)

        # Find category for the extension
        moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if ext.lower() in extensions:
                category_folder = os.path.join(source_folder, category)
                os.makedirs(category_folder, exist_ok=True)  # create if not exists
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"✅ Moved: {filename} → {category}/")
                moved = True
                break

        # If no category found → move to "Others"
        if not moved:
            other_folder = os.path.join(source_folder, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, filename))
            print(f"📂 Moved: {filename} → Others/")

def main():
    folder = input("Enter the path of the folder to organize: ").strip()
    organize_files(folder)
    print("\n🎉 File organization complete!")

if _name_ == "_main_":
    main()