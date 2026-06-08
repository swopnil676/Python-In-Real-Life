# Method 1
class numArr(object):
    def __init__(self,arr):
        self.arr = arr
    
    def returnArr(self):
        return self.arr
    
arr = numArr(
    [[1,2,3,4,5],
     [6,7,8,9,10]]
)

print(arr.returnArr()[1][1:4])
# [1] selects the second row:
# [1:4] slices from index 1 to 3 (index 4 is excluded)


# Method 2
import numpy as np

class NumArr:
    def __init__(self, arr):
        self.arr = np.array(arr)

    def returnArr(self):
        return self.arr

arr = NumArr(
    [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10]]
)

print(arr.returnArr()[1, 1:4])