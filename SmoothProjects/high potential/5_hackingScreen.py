import tkinter as tk
import random

# Window setup
root = tk.Tk()
root.title("!!! SYSTEM BREACH DETECTED !!!")

width = 1000
height = 600

root.geometry(f"{width}x{height}")
root.configure(bg="black")

canvas = tk.Canvas(
    root,
    width=width,
    height=height,
    bg="black",
    highlightthickness=0
)
canvas.pack()

# Characters for effect
chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Create falling text columns
drops = [0 for _ in range(width // 20)] 
# Divides screen into vertical columns
# Each column has a starting position (0)
# 👉 width // 20 → number of columns
# 👉 Each column is ~20 pixels apart

def draw_matrix():
    canvas.delete("all")

    for i in range(len(drops)):
        char = random.choice(chars)
        x = i * 20
        y = drops[i] * 20

        canvas.create_text(
            x, y,
            text=char,
            fill="lime",
            font=("Courier", 14, "bold")
        )

        # Reset randomly
        if y > height and random.random() > 0.975:
            drops[i] = 0

        drops[i] += 1

    root.after(50, draw_matrix)

draw_matrix()

root.mainloop()