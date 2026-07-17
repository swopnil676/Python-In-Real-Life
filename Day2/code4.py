# x = 50
# def test():
#     x = 10
#     x = 0
#     print(x)
# test()

x = 100
def test():
    global x
    x = 0
test()
print(x)