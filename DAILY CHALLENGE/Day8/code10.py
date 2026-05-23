# Method 1
marks = 32

if marks >= 35 or "grace": # False or True
    # "grace" is a non-empty string, so it is always True.
    print("passed") # True --> passed
else:
    print("not passed")



# Method 2
marks = 32
grace = True

if marks >= 35 or grace:
    print("passed")
else:
    print("not passed")
