# Questions 1
n = 7
for i in range(1, n + 1):

    # spaces
    for j in range(n - i):
        print("  ", end="")

    # numbers
    for j in range(1, i + 1):
        print(j, end="  ")

    print()

# Questions 2
effort = 8
if effort > 10:
    print("Success")
elif effort > 5:
    print("Keep Going")
else:
    print("Try Again")
