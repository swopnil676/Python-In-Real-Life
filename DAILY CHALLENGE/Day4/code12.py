# del vs .remove() vs .pop()

# Python provides three different ways to delete elements from a list:
    # del -> deletes by index or entire object (no return)
    # .remove() -> deletes by value (first occurrence)
    # .pop() -> deletes by index and returns
    # the value (default: last element)

# Syntax
# del list[index]
# list.remove(value)
# list.pop(index)      # or list.pop()

# Example
def process_list(data):
    if data:
        removed = data.pop()   # removes last element
        return removed, data
    return None, data

print(process_list([1, 2, 3]))

# Real World Use
# Removing items from user carts
# Managing queues/stacks
# Data cleaning in pipelines
# Backend APIs modifying lists