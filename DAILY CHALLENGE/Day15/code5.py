# Question 1
x = 1
if x == "Java" or "Python":
    print("Java")
else:
    print("Python")


# Question 2
    # Love calculator
name1 = input("Enter 1st name: ")
name2 = input("Enter 2nd name: ")
score = (len(name1) + len(name2)) * 7 % 100
print("Love score = ", score, "%")

    # Text repeater
text = input("Enter text : ")
times = int(input("How many times : "))
for _ in range(times):
    print(text)