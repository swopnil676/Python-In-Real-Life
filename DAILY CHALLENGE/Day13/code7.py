# 1. Using the reverse() Method
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list) # Note: reverse() modifies the original list.


# 2. Using Slicing
my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list) # Note: Creates a new reversed list.


# 3. Using the reversed() Function
my_list = [1, 2, 3, 4, 5]
reversed_list = list(reversed(my_list))
print(reversed_list) # Note: reversed() returns an iterator, so we convert it to a list.


# 4. Using a Loop with insert()
my_list = [1, 2, 3, 4, 5]
r_list = []
for i in my_list:
    r_list.insert(0, i)
print(r_list) # Logic: Each element is inserted at index 0, pushing previous elements right.


# 5. Using a Loop with append()
my_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])
print(reversed_list)