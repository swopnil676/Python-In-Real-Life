import tkinter as tk
root = tk.Tk()
root.geometry("400x200")
c = 30
f = (c*9/5)+32
tk.Label(
    root, 
    text=f"Fahrenheit: {f}",
    font=("Arial",20)
).pack(pady=50)
root.mainloop()