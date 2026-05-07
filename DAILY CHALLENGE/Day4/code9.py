n = int(input())

i = 2
flag = 0

if n < 2:
    print("Not a prime number")
else:
    while n > i:
        if n % i == 0:
            flag = 1
            break
        i += 1
    if flag == 1:
        print("Not a prime number")
    else:
        print("It's a prime number")
