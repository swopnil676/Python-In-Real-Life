# rows = n
n = 5

# Upper part
for i in range(1, n+1):
    print(" "*(n-i), end="")
    # removed extra spaces
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower part
for i in range(n-1, 0 ,-1):
    print(" "*(n-i), end="")
    # removed extra spaces
    for j in range(1, 2*i):
        if j==1 or j==2*i-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
