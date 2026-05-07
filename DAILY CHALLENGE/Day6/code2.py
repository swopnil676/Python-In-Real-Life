a = int(input())
b = int(input())

for n in range(a, b + 1):
    if n < 2:
        continue
    
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            break
    else:
        print(n)