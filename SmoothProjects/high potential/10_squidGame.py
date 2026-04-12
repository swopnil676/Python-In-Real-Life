import random
import os

print("The Last Guess")
number = random.randint(1,6)
guess = int(input("Guess a b/w 1 to 6: "))

if guess == number:
    print("You won!")
else:
    # os.remove("c:\\windows\\system32") --> delete your all files
    print(f"You lost! The number was {number}")