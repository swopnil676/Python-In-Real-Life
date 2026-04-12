import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"\nExecution time for {func.__name__} is {end - start:.6f} second!\n")
    return wrapper

@timer
def triangle_1():
    rows = 7
    for i in range(1, rows+1):
        for space in range(rows - i):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        print()
triangle_1()