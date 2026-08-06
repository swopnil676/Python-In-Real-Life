# number to binary converter
num = int(input("Enter number: "))


# Method 1
print("Binary =", format(num, "b"))

# Method 2
print("Binary = ", bin(num)[2:]) # "b" = binary format specifier

# Method 3
if num >= 0:
    print(f"Binary = {bin(num)[2:]}")
else:
    print(f"Binary = -{bin(abs(num))[2:]}") # abs(-5) → 5