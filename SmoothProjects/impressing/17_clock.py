import tkinter as tk
import time


class Main:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("900x500")
        self.root.config(bg="#fff")

        self.cur()

    def cur(self):
        self.fm3 = tk.Frame(self.root, bg="#fff", width=900, height=390)
        self.fm3.place(x=0, y=110)

        # AM/PM label
        self.lb7_hr = tk.Label(self.fm3, text="", font=("Helvetica", 40, "bold"), bg="#fff")
        self.lb7_hr.place(x=700, y=150)

        # Time label
        self.time_label = tk.Label(self.fm3, text="", font=("Helvetica", 80, "bold"), bg="#fff")
        self.time_label.place(x=150, y=100)

        self.clock()

    def clock(self):
        h = str(time.strftime("%H"))
        m = str(time.strftime("%M"))
        s = str(time.strftime("%S"))

        # AM/PM logic
        if int(h) >= 12:
            self.lb7_hr.config(text="PM")
        else:
            self.lb7_hr.config(text="AM")

        # Convert to 12-hour format
        h12 = int(h) % 12 or 12

        self.time_label.config(text=f"{h12:02}:{m}:{s}")

        # Repeat every 1 second
        self.root.after(1000, self.clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    root.mainloop()