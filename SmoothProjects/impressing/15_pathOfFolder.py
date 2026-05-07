# Day 18 of learning Python.

import os
import shutil

# path = r'Write your path here'
path = r'A:\CODING\ADVANCED PYTHON\Special_projects\SmoothProjects\impressing\15_testingFile'
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if extension:
        if not os.path.exists(path + '/' + extension):
            os.makedirs(path + '/' + extension)
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

print("\n __CLEANUP COMPLETE__")
print("Desktop Organised")



# <-- before -->
# Desktop/
# │
# ├── photo.jpg
# ├── resume.pdf
# ├── song.mp3
# ├── notes.txt
# ├── video.mp4


# <-- after -->
# Desktop/
# │
# ├── jpg/
# │   └── photo.jpg
# │
# ├── pdf/
# │   └── resume.pdf
# │
# ├── mp3/
# │   └── song.mp3
# │
# ├── txt/
# │   └── notes.txt
# │
# ├── mp4/
# │   └── video.mp4