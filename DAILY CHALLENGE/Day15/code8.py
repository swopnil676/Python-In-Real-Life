# Slice Assignment in Python
# (a[1:3] = [10, 20, 20])

# Slice assignment modifies a range of elements inside a list.
# It allows you to replace, insert, or delete multiple elements at once.
# Instead of modifying one element, you can modify a whole portion
# (slice) of the list in a single operation.

# Syntax
# list[start:end] = iterable


# Example

def clean_negatives(lst):
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            lst[i:i+1] = [0]  # slice assignment
        i += 1
    return lst


print(clean_negatives([1, -2, 3, -4]))

# Output:
# [1, 0, 3, 0]

# Real World Use
# Updating items in shopping carts
# Data cleaning pipelines
# Machine Learning preprocessing
# Batch updates in APIs