# 1: The Indexing Approach
names = ["Rahul", "Neha", "Aman"]

for i in range(len(names)):
    print(i, names[i])


# 2: The Enumerate Approach
names = ["Rahul", "Neha", "Aman"]

for index, name in enumerate(names):
    print(index, name)