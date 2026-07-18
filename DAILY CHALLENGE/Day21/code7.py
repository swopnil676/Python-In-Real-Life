text = "Python"
print(repr(text))

print(repr(10))

# repr() returns the official string representation of an object.
# Syntax: repr(object)


print("\n")


num = [1,2,3,4]

num.remove(2) # remove(value)
print(num)

num.pop(1) # pop(index)
print(num)


print("\n")


def func(x, L=[]):
    L.append(x)
    return L

print(func(1))
print(func(2))