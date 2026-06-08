import time

lives = 3

while lives > 0:
    print("Lives left:", lives)
    time.sleep(1)   # waits 1 second
    # lives -= 1
    lives =- 1

print("Game Over!")