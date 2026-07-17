email = input("Enter your email: ")
username = ""

for i in email:
    if i == "@":
        break

    username = username + i

print("Username:", username)