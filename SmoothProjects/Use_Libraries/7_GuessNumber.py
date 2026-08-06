import random

number = random.randint(1,10)
while True:
    guess = int(input("Guess number (1-10): "))

    if guess == number:
        print("Correct! You won!")
    
    elif guess < number:
        print("Too Low! Try again!")

    else:
        print("Too High! Try again!")