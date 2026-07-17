import random

quotes = [
    "Keep Coding!",
    "Never give up",
    "Learn something new today!"
]

print(random.choice(quotes)) # Learn something new today!
print(random.choices(quotes)) # ['Never give up']