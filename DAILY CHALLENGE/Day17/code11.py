squares = [x**2 for x in range(10)]
print(squares)


filtered_squares = [x for x in squares if x > 20]
print(filtered_squares)


nested_comp = [(x, y) for x in range(3) for y in range(3)]
print(nested_comp)


names = ['Alice', 'Bob', 'Charlie']
upper_names = [name.upper() for name in names]
print(upper_names)