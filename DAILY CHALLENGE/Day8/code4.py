# any() and all() in Python

# any() returns True if at least one element is True
# all() returns True only if all elements are True
# Both functions evaluate iterables like lists, tuples, or generators
# Note: all([]) returns True, any([]) returns False

# Syntax
# any(iterable)
# all(iterable)

# Example

def validate_users(users):
    if any(user == "" for user in users):
        return "Invalid user found"

    if all(len(user) > 2 for user in users):
        return "All users valid"

    return "Check users"

print(validate_users(["Sam", "Tom", "Alex"]))

# Output
# All users valid

# Real World Use
# Form validation (empty fields)
# Checking API response validity
# Data filtering in pipelines
# Machine learning preprocessing
# Security checks (permissions)