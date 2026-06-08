# a = [1, 2, 3, 4, 5] # TypeError: 'int' object is not subscriptable
a = [[1], [2], [3], [4], [5]]
b = a[:]
b[2][0] = 9
print(a)
