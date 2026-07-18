# Python Interview Question 1

try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid Input")
else:
    print("You entered:", num)




# Python Interview Question 2
ids = {id(True) for i in range(5000)}
print(ids) # a set stores only unique values = {140727636138920}