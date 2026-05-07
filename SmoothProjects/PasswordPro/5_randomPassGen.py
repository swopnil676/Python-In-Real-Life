import random
import string

# chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOP"
chars = string.ascii_letters + string.digits + string.punctuation

length = int(input("enter length: "))
password = ""

for a in range(length):
    password += random.choice(chars)

print(password)