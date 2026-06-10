# Lambda Function:- A lambda function is a small function without a name

square = lambda a: a*a
num = int(input("Enter a number: "))
print("Square = ",square(num))



# Square of list elementusing map function

nums = [1, 2, 3, 4]
square = list(map(lambda x: x * x, nums))
print("Square of list element: ",square)