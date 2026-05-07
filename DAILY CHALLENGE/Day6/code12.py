a = int(input())
b = int(input())

for num in range(a, b + 1):
    num_str = str(num)  # Convert number → string to access digits easily
    n = len(num_str)  # n = number of digits

    result = 0
    for digit_char in num_str:
        digit = int(digit_char)  # Extract each digit
        result = result + digit**n  # Raise it to power n and Add to result

    if result == num:  # f equal → Armstrong number
        print(f"{num} is a armstrong number.")


# input
# 100
# 500

# output
# 153 is an Armstrong number.
# 370 is an Armstrong number.
# 371 is an Armstrong number.
# 407 is an Armstrong number.

# Flow in simple words:
# Take number → count digits → split digits → raise each digit to power → add → compare → print if equal