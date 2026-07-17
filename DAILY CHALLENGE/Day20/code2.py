# developpers approach
print(eval(input("Enter expression: ")))
'''
User Input
     ↓
input("enter")
     ↓
Returns a string
     ↓
eval()
     ↓
Evaluates the expression
     ↓
Returns result
     ↓
int()
     ↓
Converts result to integer
     ↓
print()
     ↓
Displays output
'''

# begginers approach
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == '*':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")