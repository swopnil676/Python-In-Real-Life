import random
number = random.randint(1,10)
Guess = int(input("Guess number (1-10): "))
if Guess == number:
    print("Correct, number is also: ",number)
else:
    print("Wrong, number was : ",number)