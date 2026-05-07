import os
import time

print("...INITIALIZING THE AUTOMATION...")
time.sleep(1)

folder = "A:\CODING\ADVANCED PYTHON\Special_projects\SmoothProjects\FileOriented"

for i in range(1, 6):
    fileName = f"Project_Data_{i}.txt"
    filePath = os.path.join(folder, fileName)

    with open(filePath, 'w') as f:
        f.write("Working in progress\n")
        f.write(f"File {i} created successfully!")

    print(f">>Created: {fileName} at {os.path.abspath(filePath)}")
    time.sleep(0.05)

print("\nTask Completed....5 files organized")
