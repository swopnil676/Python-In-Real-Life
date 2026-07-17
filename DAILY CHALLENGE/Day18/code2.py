# This program simulates a simple bank
# where the user can interact using input

balance = 2000

while True:
    print("\n1-Check 2-Deposit 3-Exit")
    choice = input("Choose: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        balance += int(input("Deposit: "))

    elif choice == "3":
        break

    else:
        print("Invalid")