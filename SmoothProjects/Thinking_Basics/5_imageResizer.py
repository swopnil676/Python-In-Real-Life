from PIL import Image
import os


print("Current folder:", os.getcwd())

# Loop through files in the current directory
for f in os.listdir("."):
    if f.endswith((".jpg", ".png")):
        img = Image.open(f)
        img = img.resize((800, 600))
        img.save(f"resized_{f}")
        print(f"Resized: {f}")