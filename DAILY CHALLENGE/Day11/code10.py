# noob
nums = [False, False, True]
result = False
for i in nums:
    if i:
        result = True
        break
print(result)



# pro
nums = [False, False, True]
print(any(nums))



# example
print(any([0, 0, 5]))        # True
print(any([0, "", None]))    # False