import pyautogui as s
import time

s.press("win")
time.sleep(1)

s.write("notepad", interval=0.1)
s.press("enter")

time.sleep(1)

s.write("Hey do you know", interval=0.2)
s.press("enter")

s.write("Chini vai is a mitha", interval=0.2)
s.press("enter")
