def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
    
print(is_iterable([1,2,3]))