# Question 1:
# items = [1,2,3]
# print(items[3]) # IndexError: list index out of range



# Question 2:
num = [1,2,3,4]
for i in num:
    for j in num:
        if i != j:
            print(i, j)



# Question 3:
# From a list of numbers, move zero to the end of the list.

list = [1, 0, 2, 0, 4, 6]

for item in list:
    if item == 0:
        list.remove(item)
        list.append(item)

print(list)