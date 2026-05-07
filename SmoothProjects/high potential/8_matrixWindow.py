import tkinter as tk
import random
import winsound

root = tk.Tk()
root.title("System Breach")
root.geometry("800x500")
root.configure(bg="black")

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*?"
font_size = 15

drops = []

def draw():
    global drops

    canvas.delete("all")

    # ✅ Get current size (IMPORTANT)
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    columns = width // font_size

    # ✅ Adjust drops list dynamically
    if len(drops) < columns:
        drops += [0] * (columns - len(drops))
    elif len(drops) > columns:
        drops = drops[:columns]

    for i in range(columns):
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

        if y > height and random.random() > 0.975:
            drops[i] = 0

        drops[i] += 1

    # 🔊 Random beep
    if random.random() > 0.995:
        winsound.Beep(1000, 50)

    root.after(50, draw)

draw()

root.bind("<Escape>", lambda e: root.destroy())

root.mainloop()