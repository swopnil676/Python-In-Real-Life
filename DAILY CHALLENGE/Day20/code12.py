"""
question 1: GIVEN SORTED ARRAY nums AND target, 
RETURN 2 NUMBERS INDEX THATS SOME==TARGET
"""

#GIVEN: SORTED ARRAY
# ARGUMENTS= NUMS AND TARGET
#O/P - RETURN INDEX VALUES

def twosum(nums,target):
    for left in range(len(nums)):
        for right in range(left+1,len(nums)):
            if nums[left]+nums[right]==target:
                return (nums[left],nums[right])
    return []

nums=1,2,3,4,5
target=9
print("Two numbers are :",twosum(nums,target))