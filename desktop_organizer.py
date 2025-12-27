import os
import shutil

folders = {
    "Texts": [".txt"],
    "Music": [".mp3", ".wav", ".flac"],
    "Video": [".mp4", ".mov", ".avi"],
    "Images": [".jpg", ".png", ".gif", ".jpeg"],
    "Documents": [".pdf", ".docx", ".pptx"],
    "Executables": [".exe", ".msi", ".bat", ".lnk"],
}

path = r"C:\Users\teo\Desktop"
files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        for category, extensions in folders.items():
            filename = file.lower().strip()
            if filename.endswith(tuple(extensions)):
                folder_path = os.path.join(path, category)
                os.makedirs(folder_path, exist_ok=True)
                print(f"Would move {file_path} -> {folder_path}")
                shutil.move(file_path, folder_path)
                break
        else:
            other_folder = os.path.join(path, "Other")
            os.makedirs(other_folder, exist_ok=True)
            print(f"Would move {file_path} -> {other_folder}")
            shutil.move(file_path, other_folder)



