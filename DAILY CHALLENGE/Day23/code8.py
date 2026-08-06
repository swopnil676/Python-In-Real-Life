text = input("Enter a string: ")
char = input("Enter the character to remove: ")

result = ""

for i in text:
    if i != char:
        result = result + i

print("Updated string:", result)