car = "fast n mpg"
print(car.title())


print(int(str(12345)[::-1]))
print(int(str(12345)[::-1]))


text = input("Enter sentence : ")
words = text.split()
print("Total words = ",len(words))


import copy

a = [[1,2],[3,4]]
b = copy.copy(a)
c = copy.deepcopy(a)

a[0][0] = 100

print(b)
print(c)