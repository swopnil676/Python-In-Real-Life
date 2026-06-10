# Question 1
debug = True
items = [10, 20, 30]
if debug:
    print(f"{items = }")
    print(f"{len(items) = }")



# Question 2
    # noob
s = "hello"
chars = ()
for c in s:
    chars += (c,)
print(chars)


    # pro
s = "hello"
print(tuple(s))