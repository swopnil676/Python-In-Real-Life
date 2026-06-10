# method 1
def multiply(x, y):
    return x * y

print(multiply(25, 65))


# method 2
print(25 * 65)


# method 3
print((lambda x, y: x * y)(25, 65))
'''
lambda x, y: x * y
          │
          ▼
Anonymous function created
          │
          ▼
Called with (25, 65)
          │
          ▼
25 * 65
          │
          ▼
1625
          │
          ▼
print(1625)
'''