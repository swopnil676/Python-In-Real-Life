n = 5

for i in range(n):
    num = 1

    # print spaces
    print(" " * (n - i), end="")

    # print numbers
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i-j) // (j+1)

    print()

'''
Row 0 :        1

Row 1 :      1   1

Row 2 :    1   2   1

Row 3 :  1   3   3   1

Row 4 :1   4   6   4   1
'''