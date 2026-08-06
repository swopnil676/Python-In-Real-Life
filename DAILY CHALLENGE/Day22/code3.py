# Question 1
def add_numbers(a, b):
    return a+b

numbers = [(1,2), (3,4), (5,6)]

results = [add_numbers(a,b) for a, b in numbers]
print(results)




# Question 2
expences = []
while True:
    amount = input("Enter expences or exit : ")
    if amount == "exit":
        break
    expences.append(float(amount))

print("Total Expences : ", sum(expences))
