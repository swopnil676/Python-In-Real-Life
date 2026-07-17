from collections import Counter

alphabets = ['b', 'c', 'b', 'a', 'c', 'a']

grouped = list(Counter(alphabets).elements())

# Counter({'b': 2, 'c': 2, 'a': 2})
# .elements() returns an iterator that repeats each element according to its count : b, b, c, c, a, a

print(grouped)