    # not give that's output
def add_item(item, my_list=[]):
    my_list.append(item)
    return my_list
print("Previous Output:")
print(add_item(1))
print(add_item(2))
print(add_item(3))

    # give the output
def add_item(item, my_list=None):
    if my_list == None:
        my_list = []
    my_list.append(item)
    return my_list
print("New Output:")
print(add_item(1))
print(add_item(2))
print(add_item(3))