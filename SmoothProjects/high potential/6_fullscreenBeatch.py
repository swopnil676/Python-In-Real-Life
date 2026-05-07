import tkinter as tk
import random
import time
import winsound

root = tk.Tk()
root.title("System Breach")
root.attributes("-fullscreen",True)
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ✅ FIX: use pixel dimensions
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?"
font_size = 15
columns = width // font_size

drops = [0 for _ in range(columns)]

# Drawing function
def draw():
    canvas.delete("all")

    for i in range(len(drops)):
        char = random.choice(chars)
        x = i * font_size
        y = drops[i] * font_size

        canvas.create_text(
            x, y,
            text=char,
            fill="#00ff00",
            font=("Consolas", font_size, "bold"),
            anchor="nw"
        )

        # Reset randomly
        if y > height and random.random() > 0.975:
            drops[i] = 0

        drops[i] += 1

    # Optional glitch sound
    if random.random() > 0.995:
        winsound.Beep(1000, 50)

    root.after(50, draw)

# Start animation
draw()

# Exit on ESC
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()