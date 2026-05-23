# Method 1
list = [3, 1, 2]

list.sort()  # sorts the original list
sorted(list)  # creates a new sorted list (not stored)

print(list)


# Method 2
nums = [3, 1, 2, 5, 9, 4]

new_nums = sorted(nums)

print(nums)
print(new_nums)
