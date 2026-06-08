# Question 1
for i in range(3,0,-1):
    print(i)


# Question 2
s = "Python"
s = s[::-2] # string[start:stop:step]
print(s)
# start = end of string (default because step is negative)
# stop = beginning of string (default)
# step = -2 (move backward by 2 positions)


# Question 3
x = [[1],[2],[3]]
y = x*2
y[0].append(99)
print(y)