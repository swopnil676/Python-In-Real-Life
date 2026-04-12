import tkinter as tk
from tkinter import messagebox

def show_message():
    print("Button clicked!")
    messagebox.showinfo("Message", "You clicked the button!")

root = tk.Tk()

root.title("Tkinter Demo App")
root.geometry("380x280")

label = tk.Label(root, text = "Follow Me", font=("Arial",19))

label.pack(pady=40)

button = tk.Button(root, text="click me!", command=show_message)
button.pack( )

root.mainloop()