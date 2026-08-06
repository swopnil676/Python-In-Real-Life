# Junior Approach
items = [1, 2, 2, 3, 1]
unique_items = []
for i in items:
    if i not in unique_items:
        unique_items.append(i)
print(unique_items)




# Senior Approach
items = [1, 2, 2, 3, 1]
print(list(dict.fromkeys(items)))