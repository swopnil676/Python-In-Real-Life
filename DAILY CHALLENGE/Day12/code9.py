# Question 1
st = int(input("Start : "))
end = int(input("End : "))
for i in range(st, end + 1):
    print(i)

# Question 2
for i in range(3):
    print(i)
else:
    print("Done")

# Question 3
name = "sara"
age = 8

if age > 5:
    if age == 8:
        print(f"{name} is a Teen")
    else:
        print(f"{name} is a Child")
print(f"{name} is done")
