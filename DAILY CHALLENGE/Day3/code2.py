nums = [1,2,3,4]

result = [i*j for i in nums for j in nums if i%2 == 0]
print(result)