i = 0
while i < 5:
    correct_password = 1234
    password = int(input("enter your password: "))
    if password == correct_password:
        print('''correct password
your account Logged in''')
        A = open("Your_File.txt", 'w')
        saved = str(password)
        p = A.write(saved)
        print("your password has been saved")
    else:
        i += 1
        print("incorrect")
        if i == 5:
            break