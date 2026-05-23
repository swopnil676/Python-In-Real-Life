# Wrong code:
x = 5
if 1 < x < 10:
    print("in range")
elif x == 5 or 6:
    print("five or six")
else:
    print("out of range")


# Right code:
x = 5
if 1 < x < 10:
    print("in range")
# elif x == 5 or x == 6:
elif x in [5, 6]:
    print("five or six")
else:
    print("out of range")

# note:
# For x = 5, first condition still runs first, so output remains: in range