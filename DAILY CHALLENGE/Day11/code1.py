import numpy as np

lst = []
for i in range(1, 6):
    lst.append(i)

arr1 = np.array(lst)  # arr1 = [1 2 3 4 5]
arr2 = np.ones((5,))  # arr2 = [1. 1. 1. 1. 1.]
arr3 = np.arange(1, 6)  # arr3 = [1 2 3 4 5]

result = arr1 + arr2 + arr3 # [ 3.  5.  7.  9. 11.]
# 1+1+1 = 3
# 2+1+2 = 5
# 3+1+3 = 7
# 4+1+4 = 9
# 5+1+5 = 11

print(result)
print(result.dtype)
