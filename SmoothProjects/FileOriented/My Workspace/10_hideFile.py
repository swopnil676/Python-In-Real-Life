import os

file = r"A:\CODING\ADVANCED PYTHON\Special_projects\SmoothProjects\FileOriented\FileOriented/Project_Data_5.txt"
password = "1234"

if input("Enter password: ") == password:
    
    choice = input("Type 'h' to hide or 'u' to unhide: ").lower()

    if choice == 'h':
        os.system(f'attrib +h "{file}"')
        print("File Hidden 🔒")

    elif choice == 'u':
        os.system(f'attrib -h "{file}"')
        print("File Visible 🔓")

    else:
        print("Invalid choice!")

else:
    print("Wrong password ❌")