cart = ["Laptop", "Mouse", "Keyboard"]
print(" | ".join(cart))


print("Hello" * 3)
# output: HelloHelloHello


# METHOD WITHOUT lambda
def add(x, y):
    return x + y
print(add(1, 2))

# METHOD WITH lambda
print((lambda x, y: x + y)(1, 2))
