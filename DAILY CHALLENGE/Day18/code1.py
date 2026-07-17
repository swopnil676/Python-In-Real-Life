# question 1
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0][0] = 99

print(a)
print(b)


# question 2
nums = [1, 2, 3, 4]
for i in range(len(nums)):
    nums[i] *= 2

print(nums)


# question 3
n = 1
for i in range(1, 6):
    n = n + i * i
print(int(n**0.5))
