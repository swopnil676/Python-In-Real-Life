names = ["Swopnil","Trisha"]
age = [20,19]

    # Method 1 -> gives error
# pairs = []
# for i in range(len(names)):
#     pairs.append(names[i],age[i])
# print(pairs)

    # Method 2 -> no error
print(list(zip(names, age)))