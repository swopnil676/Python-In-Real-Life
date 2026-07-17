import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+-="

password=""

for i in range(8):
    password+=random.choice(chars)

print("Genereted Password:",password)