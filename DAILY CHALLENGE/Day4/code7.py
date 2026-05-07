a = [1,2,3]
b = [1,2,3]
c = a

print(a is c)   # True (same object)
print(a == c)   # True (same values)

print(a == b)   # Both lists have same elements → True
print(a is b)   # a and b are two different list objects → False