text = input("Enter text: ")
result = "".join(reversed(text.upper()))
print("Reversed Output:", result)



# Square Root Finder : 
num = float(input("ENter number : "))
print("Square root = " , num ** 0.5)



a = "listen"
b = "silent"
print(sorted(a) == sorted(b))



a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(9)
print(a[0], len(b))