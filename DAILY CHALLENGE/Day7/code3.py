message = "hi" # Since "hi" is non-empty:

'''
if message

becomes: if True

So Python enters the if block.
'''
if message: 
    print(message == "Hello")
else:
    print("Empty")

'''
Then this line runs: print(message == "Hello")

Checks: "hi" == "Hello"

Which is: False
'''
