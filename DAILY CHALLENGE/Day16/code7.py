# *args vs **kwargs
# *args and **kwargs are special Python syntax used to pass a variable number of arguments into functions.
# Python Syntax
# *args
def args_func(*args):
    print(args)

# **kwargs
def kwargs_func(**kwargs):
    print(kwargs)


# Example

def order_system(*items, **details): 
# *items     # tuple
# **details  # dictionary

    print("Items:")
    for item in items:
        print("-", item)

    print("\nCustomer Details:")
    for key, value in details.items():
        print(f"{key}: {value}")


order_system(
    "Pizza",
    "Burger",
    "Coke",
    name="Rob",
    city="Dallas"
)