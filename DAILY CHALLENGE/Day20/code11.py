n = 7
for i in range(n):
    for j in range(n):
        print("*" if j == i or j == n - 1 - i
              else " ", end="")
    print(" " * (n - 2), end="")
    for j in range(n):
        print("*" if j == i or j == n - 1 - i
              else " ", end="")
    print()

for i in range(n // 2 - 1, -1, -1):
    for j in range(n):
        print("*" if j == i or j == n - 1 - i
              else " ", end="")
    print(" " * (n - 2), end="")
    for j in range(n):
        print("*" if j == i or j == n - 1 - i
              else " ", end="")
    print()