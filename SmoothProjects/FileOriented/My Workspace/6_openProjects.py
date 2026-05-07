import os
import time

print("🚀 SMART PROJECT GENERATOR INITIALIZING...\n")
time.sleep(1)

# 🔹 Take user input
project_name = input("Enter your project name: ").strip()

# Base directory
base_path = os.path.join(os.getcwd(), project_name)

# 🔹 Folder structure
folders = ["src", "docs", "data", "tests"]

# 🔹 Files with content
files = {
    "README.md": f"# {project_name}\n\nProject initialized successfully 🚀",
    "src/main.py": '''def main():
    print("Hello from your project!")

if __name__ == "__main__":
    main()
''',
    ".gitignore": "__pycache__/\n*.pyc\n.env\n"
}

# 🔹 Create main project folder
os.makedirs(base_path, exist_ok=True)
print(f"\n📁 Created project folder: {project_name}")
time.sleep(0.5)

# 🔹 Create subfolders
for folder in folders:
    path = os.path.join(base_path, folder)
    os.makedirs(path, exist_ok=True)
    print(f">> Created folder: {folder}")
    time.sleep(0.1)

# 🔹 Create files
for file, content in files.items():
    file_path = os.path.join(base_path, file)
    
    # Ensure folder exists (for nested files like src/main.py)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f">> Created file: {file}")
    time.sleep(0.1)

print("\n✅ Project setup complete!")
print(f"📍 Location: {base_path}")
print("\n🔥 Ready to build something awesome!")


# AI_App/
# │
# ├── src/
# │   └── main.py
# ├── docs/
# ├── data/
# ├── tests/
# ├── README.md
# └── .gitignore