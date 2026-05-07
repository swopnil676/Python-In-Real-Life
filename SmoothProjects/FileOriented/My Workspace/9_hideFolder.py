import os

folder = r"A:\CODING\ADVANCED PYTHON\Special_projects\SmoothProjects\FileOriented\AI APP"
password = "1234"

if input("Enter password: ") == password:
    
    choice = input("Type 'h' to hide or 'u' to unhide: ").lower()

    if choice == 'h':
        os.system(f'attrib +h "{folder}"')
        print("Folder Hidden 🔒")

    elif choice == 'u':
        os.system(f'attrib -h "{folder}"')
        print("Folder Visible 🔓")

    else:
        print("Invalid choice!")

else:
    print("Wrong password ❌")