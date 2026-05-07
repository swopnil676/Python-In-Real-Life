import pyfiglet
import time

text = "JOLU ECE"
ascii_art = pyfiglet.figlet_format(text,font="big")
for text in ascii_art:
    print(text, end='', flush=True)
    time.sleep(0.002)

print("initializing vision....")
time.sleep(1)

# print(ascii_art)
print("Empire building in process")