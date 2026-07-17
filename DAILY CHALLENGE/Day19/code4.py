x = [1, 2, [3, 4], 5]

x[2][1] = 10 # 4 will be replaced with 10.
x.append([20, 30])

x[0], x[3] = x[3], x[0] # x[0], x[3] = 5, 1

    # Visualization:
# Before:
# [1, 2, [3,10], 5, [20,30]]

# Swap index 0 and 3

# After:
# [5, 2, [3,10], 1, [20,30]]


print(x)
print(x[2][0])
print(x[-1][1])
