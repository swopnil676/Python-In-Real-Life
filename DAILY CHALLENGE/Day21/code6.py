import random

a = random.randint(1, 10)
b = random.randint(1, 10)

print(f"what is the sum of {a} + {b}?")

user_answer = int(input("Your Answer: "))

if (a + b) == user_answer:
    print("correct")
else:
    print("wrong")