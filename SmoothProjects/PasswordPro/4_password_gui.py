import secrets
import string
import tkinter as tk
from tkinter import messagebox

# 🔹 Generate password function
def generate_password():
    length = length_var.get()

    use_lower = lower_var.get()
    use_upper = upper_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    alphabet = ""
    password = []

    if use_lower:
        alphabet += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))

    if use_upper:
        alphabet += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))

    if use_digits:
        alphabet += string.digits
        password.append(secrets.choice(string.digits))

    if use_symbols:
        alphabet += string.punctuation
        password.append(secrets.choice(string.punctuation))

    # ❌ Validation
    if not alphabet:
        messagebox.showerror("Error", "Select at least one option!")
        return

    if length < len(password):
        messagebox.showerror("Error", "Length too short!")
        return

    # Fill remaining
    for _ in range(length - len(password)):
        password.append(secrets.choice(alphabet))

    # Shuffle
    secrets.SystemRandom().shuffle(password)

    # Final password
    final_password = ''.join(password)
    password_var.set(final_password)


# 🔹 Copy to clipboard
def copy_password():
    pwd = password_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")


# 🔹 GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# 🔹 Variables
length_var = tk.IntVar(value=12)
lower_var = tk.BooleanVar(value=True)
upper_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)
password_var = tk.StringVar()

# 🔹 UI Elements
tk.Label(root, text="Password Length", font=("Arial", 12)).pack(pady=5)

tk.Scale(root, from_=4, to=32, orient="horizontal", variable=length_var).pack()

tk.Checkbutton(root, text="Lowercase", variable=lower_var).pack()
tk.Checkbutton(root, text="Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Digits", variable=digits_var).pack()
tk.Checkbutton(root, text="Symbols", variable=symbols_var).pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=10)

tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30, justify="center").pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_password).pack(pady=5)

# 🔹 Run app
root.mainloop()