numbers = [1, 2, 3, 4, 5]

squared = [x ** 2 for x in numbers]

print(squared)

filtered_squares = [x for x in squared if x > 10]

print(filtered_squares)