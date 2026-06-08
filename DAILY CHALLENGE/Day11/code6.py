data = ["MI", "RCB", "CSK", "KKR", "CSK"]
result = list(
    dict.fromkeys(data)
)  # Removes duplicates because dictionary keys must be unique.
result.pop(1)  # Removes element at index 1.
print(result)
