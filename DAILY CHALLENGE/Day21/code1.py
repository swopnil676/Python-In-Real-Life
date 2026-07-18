data = ["Python", "Java", "C++", "Go", "Rust"]
fs = frozenset(data)

print(fs.copy())


other = frozenset(["Python", "Ruby"])

print(fs.union(other))
print(fs.intersection(other))
print(fs.difference(other))
print(fs.issubset(other))