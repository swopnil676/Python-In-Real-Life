# Method 1
# import time
# from itertools import cycle

# lights = [
#     ('Green', 2),
#     ('Yellow', 0.5),
#     ('Red', 2)
# ]

# colors = cycle(lights)

# while True:
#     c,s = next(colors)
#     print(c)
#     time.sleep(s)



# Method 1
import time

lights = [
    ('Green', 2),
    ('Yellow', 0.5),
    ('Red', 2)
]

i = 0
while True:
    c,s = lights[i]
    print(c)
    time.sleep(s)
    if i == len(lights)-1:
        i = 0
    else:
        i += 1