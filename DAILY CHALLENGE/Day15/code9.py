import numpy as np

x = np.array([1, 2, 3, 5, 6])
n = 6

missing_num = n * (n + 1) // 2 - np.sum(x)
print(f"Missing number is {missing_num}")
