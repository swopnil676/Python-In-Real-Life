import random

items = ["rock", "paper", "scissor"]
computer = random.choice(items)

user = input("Rock Paper Or Scissor: ").lower()

print("COMPUTER CHOOSES", computer)

if user == computer:
    print("Match Draw......!")

# cases of user
elif user == "rock" and computer == "scissor":
    print("User Winnnn!!!!!")
elif user == "paper" and computer == "rock":
    print("User Winnnn!!!!!!")
elif user == "scissor" and computer == "paper":
    print("User Winnnn!!!!")

# cases of computer
else:
    print("Computer Win####")