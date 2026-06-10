# Set Operations - Union |, Intersection &, Difference -
# Set operations in Python are used to:
# combine unique values from sets
# compare sets
# find common values
# remove duplicates
# find differences between collections
# Sets are unordered collections of unique values.

# Syntax

# Union Operator
# a | b

# Intersection Operator
# a & b

# Difference Operator
# a - b


# Example

user1 = {"sam", "john", "alex", "mike"}
user2 = {"alex", "mike", "robin"}

print("All Followers:", user1 | user2)
print("Common Followers:", user1 & user2)
print("Only User1 Followers:", user1 - user2)

# Real World Use
# Social Media Apps
# Data Engineering
# Cybersecurity
# AI/ML Systems