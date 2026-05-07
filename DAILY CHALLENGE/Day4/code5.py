# noob
nums = [5,1,4,2,3]
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i]> nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
print(nums)


# pro
nums = [5,1,4,2,3]
print(sorted(nums))