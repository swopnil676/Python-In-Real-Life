# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Create a new list with squares using list comprehension
squares = [x**2 for x in numbers]

# Use list comprehension with an if condition
filtered_squares = [x**2 for x in numbers if x % 2 == 0]

# Print the results
print('Squares:', squares)
print('Filtered Squares:', filtered_squares)




