# Question 1
teams = ("mi", "rcb", "csk", "kkr")
print(teams[::-1].index("mi"))


# Question 2
def check(data):
    if len(data) > 2:
        print("big list")
    else:
        print("small list")


check(["hello/n"])


# Question 3
x = [10, 20, 30, 40]
for i in range(1, 3):
    x[i] += 5
print(x)


# Question 4
a = [[1, 2],[3, 4]]
b = a.copy()
b[0][0] = 99
print(a)
print(b)
