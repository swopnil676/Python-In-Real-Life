import os
import time
import pyautogui

print("System armed. Move the mouse to lock the PC.")
last_position = pyautogui.position()

while True:
    current_position = pyautogui.position()
    
    if current_position != last_position:
        print("Movement detected! Locking system...")
        os.system("rundll32.exe user32.dll,LockWorkStation")
        break
        
    time.sleep(0.1)  # Pauses for 100ms so your CPU can breathe