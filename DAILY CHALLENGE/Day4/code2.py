# What is enumerate()
# enumerate() is a built-in Python function that
# adds a counter (index) to an iterable and returns
# it as an enumerate object (iterator of tuples).
# enumerate() solves this by:
# Automatically tracking index
# Makes code cleaner, more readable and Pythonic..

# Syntax
# enumerate(iterable, start=0)

data = ["a", "b", "c"]

# Default enumerate
for i, val in enumerate(data):
    print(i, val)

# Custom start index
for i, val in enumerate(data, start=1):
    print(i, val)

# Example
menu = ["Pizza", "Burger", "Pasta"]
for i, item in enumerate(menu, start=1):
    print(f"{i}. {item}")




# Real World Use:--
# UI menus (numbered lists)
# Data processing pipelines
# Machine Learning datasets indexing
# Backend APIs (tracking records)