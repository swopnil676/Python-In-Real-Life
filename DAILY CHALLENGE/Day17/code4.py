def add_to_list(value, target_list=[]):
    target_list.append(value)
    return target_list

result1 = add_to_list(1)
result2 = add_to_list(2)

print("Result 1:", result1)
print("Result 2:", result2)

import sys

try:
    print(sys.maxsize + 1)
except OverflowError:
    print("Overflow! Python handles large ints gracefully")

# sys.maxsize: This represents the maximum value a variable of Python's internal pointer type can hold. On standard 64-bit systems, this number is $2^{63} - 1$, or 9223372036854775807.
# In languages like C++, adding 1 to a maximum integer value causes a buffer overflow, which either crashes the application or causes the number to wrap around into a negative value.
# Python's Behavior: Python automatically converts integers that outgrow standard hardware registers into an object known as an "arbitrary-precision integer." It uses as much system memory as necessary to represent the number accurately.
# The Result: The math sys.maxsize + 1 completes flawlessly. Because no OverflowError is ever raised, the except block is completely ignored, and it successfully prints the exact big number: 9223372036854775808