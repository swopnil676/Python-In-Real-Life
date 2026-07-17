rows = [
    ["name", "email", "department"],
    ["Mike", "m@example.com", "HR"],
    ["Liz", "l@example.com", "IT"]
]

row_iterator = iter(rows)

header = next(row_iterator)

print(header)
print("-" * 35)

for row in row_iterator:
    print(row)