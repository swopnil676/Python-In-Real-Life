import tkinter as tk
import random
import winsound  # Windows only

root = tk.Tk()
root.title("System Breach")

# ✅ Small window
window_width = 800
window_height = 500
root.geometry(f"{window_width}x{window_height}")
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?"

font_size = 15
columns = window_width // font_size
drops = [0 for _ in range(columns)]

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

        if y > window_height and random.random() > 0.975:
            drops[i] = 0

        drops[i] += 1

    # 🔊 Random beep effect
    if random.random() > 0.995:
        winsound.Beep(1000, 50)

    root.after(50, draw)

draw()

# Exit with ESC
root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()