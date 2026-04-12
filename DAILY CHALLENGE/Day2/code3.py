nums = [5, 12, 7, 20, 3, 15]
new_list = []
for i in nums:
    if i % 2 == 0:
        square = i ** 2
        if square < 50:
            new_list.append(square)
print(new_list)
