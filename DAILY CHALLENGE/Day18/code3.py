# Question 1
# a = [c.upper() for c in "python"] # list
a = "".join(c.upper() for c in "python") # string
print(a)

print("python".upper())


# Question 2
text = input("Enter text: ")

upper = 0
lower = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
