# Question 1
import random
result = random.choice(["Heads","Tails"])
print("Results :",result)


# Question 2
score = 0
def add_point():
    global score  # Tells Python to use the outer 'score' variable
    score += 1

add_point()
print(score)