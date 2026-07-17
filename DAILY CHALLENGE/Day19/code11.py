x = [1, 2, 3]
y = x
y.append(4)
x = [10, 20]
y.append(30)
print(x)
print(y)



def A(x):
    return x+1

def B(x):
    return x*2

print(B(A(3)))
