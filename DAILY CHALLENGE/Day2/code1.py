a = (1,2,3)

    # Given error
# a[0] = 10
# print(a)    
#TypeError: 'tuple' object does not support item assignment

    # No error
a = list(a)
a[0] = 10
print(a)