from itertools import groupby

employee = ["Rahul", "Varun", "surya", "ravi", "sai", "rani", "Visal", "Vivek"]
employee.sort() # ['Rahul', 'Varun', 'Visal', 'Vivek', 'rani', 'ravi', 'sai', 'surya']

e_grouped = groupby(employee, key=lambda i: i[0]) # lambda i: i[0] → takes the first character of each name.
for key, group in e_grouped: 
    print(key, list(group))
