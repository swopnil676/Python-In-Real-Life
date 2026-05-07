fruits = ["apple","banana","mango","kiwi","grape"]
for f in fruits: #
    if "a" in f:
        fruits.remove(f)
print(fruits) # ['banana', 'kiwi']
''' When removing:
elements shift left
But loop index still moves forward.
So some elements are skipped.

Remove item →
List shifts ←
Loop moves →
One item skipped ❌ '''



fruits = ["apple","banana","mango","kiwi","grape"]
for f in fruits[:]:  
    # fruits[:] => This creates a copy of the list.
    # The loop reads from the copy, while removals happen in the original list.
    if "a" in f:
        fruits.remove(f)
print(fruits) # ['kiwi']




fruits = ["apple","banana","mango","kiwi","grape"]
fruits = [f for f in fruits if "a" not in f]
print(fruits) # ['kiwi']