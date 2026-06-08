# noob
nums = (5, 1, 4, 2, 3)

lst = list(nums)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

sorted_tuple = tuple(lst)

print(sorted_tuple)


# pro
nums = (5, 1, 4, 2, 3)

print(tuple(sorted(nums)))