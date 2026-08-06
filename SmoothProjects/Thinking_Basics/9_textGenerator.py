import pyfiglet

text = input("Enter text: ")

fonts = ["slant", "banner", "big", "block"]

print("\nAvailable Fonts:")
for font in fonts:
    print("-", font)

font = input("\nEnter font name: ").lower()

if font == "":
    print("Font name cannot be empty!")
elif font not in fonts:
    print("Invalid font!")
else:
    print("_" * 35)
    print(" " * 10 + "Design")
    
    ascii_art = pyfiglet.figlet_format(text, font=font)
    
    print(ascii_art)
    print(f"Font = {font}")
    print("_" * 35)