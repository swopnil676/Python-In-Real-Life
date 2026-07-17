# filter() → selects elements based on a condition.
# map() → transforms each element.
# lambda → creates a small anonymous function.

nums = [1, 2, 3, 4, 5]

# filter(): keep only even numbers
evens = list(filter(lambda x: x % 2 == 0, nums))

# map(): square every number
squares = list(map(lambda x: x ** 2, nums))

print("Original:", nums)
print("Filter:", evens)
print("Map:", squares)