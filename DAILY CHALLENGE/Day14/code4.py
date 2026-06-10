nums = [3, 7, 2, 9, 5]
largest = nums[0]
second_largest = nums[0]

for i in nums:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)

'''
Note:
This code works for the given list, but it can fail for some cases (for example, all negative numbers or duplicate values). A more robust version is:
'''

nums = [3, 7, 2, 9, 5]

largest = float('-inf')
second_largest = float('-inf')

for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print(second_largest)