# Scientific Calculator
import math

num = float(input("Enter Number: "))

print("Square Root:", math.sqrt(num))
print("Sin:", math.sin(num))
print("Cos:", math.cos(num))

# Factorial only for non-negative integers
if num >= 0 and num.is_integer():
    print("Factorial:", math.factorial(int(num)))
else:
    print("Factorial: Not defined for negative numbers or decimals")