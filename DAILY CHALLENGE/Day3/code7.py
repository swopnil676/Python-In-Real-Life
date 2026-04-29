# noob
items = [1,2,3,4,5,4,3,2,1]
unique_items = []
for i in items:
    if i not in unique_items:
        unique_items.append(i)
print(unique_items)

# pro
items = [1,2,3,4,5,4,3,2,1]
print(list(dict.fromkeys(items)))