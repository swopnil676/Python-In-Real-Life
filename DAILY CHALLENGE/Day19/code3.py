def demo(a, b, *args, **kwargs):
    print("a =", a)
    print("b =", b)
    print("args =", args)
    print("kwargs =", kwargs)

demo(10, 20, 30, 40, 50, x=100, y=200)