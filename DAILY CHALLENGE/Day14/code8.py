# global vs nonlocal
# global and nonlocal are Python keywords used to
# modify variables outside the current function scope.
# Python creates a new local variable inside functions by default.

# Syntax

x = 10

def change():
    global x
    x = 20

change()

print(x)


# Example

balance = 1000

def bank():

    transactions = 0

    def deposit(amount):
        global balance
        nonlocal transactions

        balance += amount
        transactions += 1
 
        print("Balance:", balance)
        print("Transactions:", transactions)
    
    deposit(500)   # Call the function

bank()

    # Variable Scopes
# Global Scope
# │
# └── bank()
#     │
#     └── transactions = 0
#          │
#          └── deposit()
#               │
#               └── nonlocal transactions
#                    │
#                    └── use bank's transactions