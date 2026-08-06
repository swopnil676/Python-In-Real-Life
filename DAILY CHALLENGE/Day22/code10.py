# Notes App :
note = input("Write your note : ")
with open("notes.txt", "a") as file:
    file.write(note + "\n")
print("Note Saved")