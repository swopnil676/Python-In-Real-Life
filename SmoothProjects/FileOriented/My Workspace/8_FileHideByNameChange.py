import os

# ✅ Correct path (cleaned)
file_path = r"A:\CODING\ADVANCED PYTHON\Special_projects\SmoothProjects\FileOriented\Project_Data_5.txt"

# Get directory
dir_path = os.path.dirname(file_path)

# ✅ Proper names
locked_path = os.path.join(dir_path, "System_Config.txt")
unlocked_path = file_path

# 🔄 Toggle logic
if os.path.exists(unlocked_path):
    os.rename(unlocked_path, locked_path)
    print(">> File Locked 🔒")
elif os.path.exists(locked_path):
    os.rename(locked_path, unlocked_path)
    print(">> File Unlocked 🔓")
else:
    print("⚠️ File not found!")

print("Our privacy, Our power 💪")