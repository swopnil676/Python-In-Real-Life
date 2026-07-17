funcs = [lambda x: x * i for i in range(3)]
result = [f(2) for f in funcs]
print(result) # [4, 4, 4]



#Error handling

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))
    calc = n/d
    print(calc)

except ZeroDivisionError:
    print("Cannot be divided by zero")
except ValueError:
    print("Cannot have words")