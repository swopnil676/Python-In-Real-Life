n = int(input("Enter the bnumber of terms: "))
a, b = 0, 1
print(a, end=" ")
for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a, b = b, c
