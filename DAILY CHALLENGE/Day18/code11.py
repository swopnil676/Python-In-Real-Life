# Method 1
nums = [1,2,3,4]
result = list(filter(lambda x: x>2, nums))
# filter() keeps only the elements for which the function returns True.

print(result)



# Method 2
nums = [1, 2, 3, 4]
result = []

for x in nums:
    if x > 2:
        result.append(x)

print(result)



# Method 3
nums = [1, 2, 3, 4]

result = [x for x in nums if x > 2]

print(result)