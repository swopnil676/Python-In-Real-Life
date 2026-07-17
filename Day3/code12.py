    # Method 1
import math

def is_prime(n):
    if n<= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

input = input("Number to check: ")
print(f"{input=}: {is_prime(int(input))}")



    # Method 2
# n = int(input("Enter a number: "))
# if n<=1:
#     print("Not a prime number")
# else:
#     for i in range(2, int(n**0.5)+1):
#         if n%i==0:
#             print("Not a prime number")
#             break
#     else:
#         print("A prime number")