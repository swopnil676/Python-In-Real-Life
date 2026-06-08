numbers = [1, 2, 3, 4, 5]
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)


name = 'Python'
reversed_name = name[::-1]
print(reversed_name)


number_str = '12345'
digits_sum = sum(map(int, number_str))
# Equivalent to :- [int(ch) for ch in number_str]
print(digits_sum)


unique_items = set([1, 2, 2, 3, 4, 4]) # Convert the list to a set
print(unique_items)
 

product = 1
for val in [1, 2, 3, 4]:
    product *= val
print(product)