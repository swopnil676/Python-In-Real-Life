# Program 1: Directly using global variable
global_var = 10
def func():
    ans = 0
    for i in range(1000):
        ans += global_var * i
    return ans

print(func()) # Inside every iteration, Python looks up global_var from the global scope



# Program 2: Copying global variable to a local variable
global_var = 10
def func():
    ans = 0
    local_var = global_var
    for i in range(1000):
        ans += local_var * i
    return ans

print(func()) # Here, global_var is accessed only once