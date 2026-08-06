import os
import shutil

folder_path = r"C:\Users\swopn\Desktop"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Programs": [".exe"]
}

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        extension = os.path.splitext(file)[1].lower()

        for category, extensions in file_types.items():

            if extension in extensions:

                category_folder = os.path.join(folder_path, category)

                os.makedirs(category_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(category_folder, file)
                )

                print(f"Moved {file} -> {category}")
                break

print("Desktop cleaned successfully!")