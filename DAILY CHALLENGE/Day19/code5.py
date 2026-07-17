users = [
    {"name": "Ava", "age": 25},
    {"name": "Leo", "age": 20},
    {"name": "Zoe", "age": 22}
]
print(users)

# Sort by a single key ("age")
sorted_users = sorted(users, key=lambda x: x["age"])
print(sorted_users)

# Sort by multiple keys — first by age, then by name
multi_sorted_users = sorted(users, key=lambda x: (x["age"], x["name"]))
print(multi_sorted_users)
