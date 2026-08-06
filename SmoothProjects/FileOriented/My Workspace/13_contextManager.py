# --- Without context manager ---
f = open(r"A:\CODING\ADVANCED PYTHON\SmoothProjects\File_Oriented\My Workspace\data.txt", 'r')
data = f.read()
f.close()  # Easy to forget!

# --- With context manager ---
with open(r"A:\CODING\ADVANCED PYTHON\SmoothProjects\File_Oriented\My Workspace\data.txt", 'r') as f:
    data = f.read()  # Auto-closes!
print(data)

# --- Real-World Example: Writing safely ---
with open(r"A:\CODING\ADVANCED PYTHON\SmoothProjects\File_Oriented\My Workspace\log.txt", 'w', encoding='utf-8') as f:
    f.write('Hello, Python!')
    f.write('\nStay consistent, keep growing! 🚀')