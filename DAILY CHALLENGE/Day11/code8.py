a = [10, 20, 5, 40, 30]

largest = second = float('-inf') # float('-inf') means negative infinity in Python.

for i in a:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)


# <-- HOW IT WORKS -->
# Initialize largest and second with -inf
# If current number is greater than largest:
# update second = largest
# update largest = current
# Else if current number is greater than second
# and not equal to largest, update second