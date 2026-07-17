# Question 1
import random

names = ["Harry", "Jhon", "Rahul", "Priya"]
print("Winner is : ", random.choice(names)) # Priya
print("Winner is : ", random.choices(names)) # ['Priya']



# Question 2
nums=[1,2,3,4,5]

for num in nums:
    if num==3:
        print("Found 3! Stopping loop.")
        break
else:
    print("Loop Completed")