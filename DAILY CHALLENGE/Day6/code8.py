n = 5

# upper part
for i in range(1, n + 1):  # i controls the number of rows (1 → 5)
    for j in range(1, i + 1):
        print(j, end=" ")  # prints numbers from 1 to i
    print()

# lower part
for i in range(n - 1, 0, -1):  # Starts from 4 down to 1
    for j in range(1, i + 1):
        print(j, end=" ")  # Same logic prints decreasing rows
    print()
