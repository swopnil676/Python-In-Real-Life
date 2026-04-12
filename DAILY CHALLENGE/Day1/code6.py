nums = [1,2,3,4]

# noob
reversed_list = []
n = len(nums)
for i in range(n-1, -1, -1):
    reversed_list.append(nums[i])
print(reversed_list)

# pro
print(nums[::-1])
# or,
print(list(reversed(nums)))