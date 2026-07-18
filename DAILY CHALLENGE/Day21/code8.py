users = {"Ali": "pass123",
         "Sara": "secret456"}

login = input("Login as: ")
password = input("Enter password: ")

print(users[login])



text = input("Enter a string: ")
char = input("Enter a character: ")

for i in range(len(text)):

    if text[i] == char:
        print("Character found at index:", i)
        break