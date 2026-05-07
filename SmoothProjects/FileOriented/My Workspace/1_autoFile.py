import os
import time

print("...INITIALIZING THE AUTOMATION...")
time.sleep(1)

for i in range(1, 6):
    fileName = f"Project_Data_{i}.txt"
    with open(fileName, 'w') as f:
        f.write("Working in progress")
        f.write(f"File {i} created successfully!")
    
    print(f">>Created:{fileName}")
    time.sleep(0.05)

print("\nTask Completed....5 files organized")