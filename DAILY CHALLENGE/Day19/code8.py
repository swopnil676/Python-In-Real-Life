# Method 1
products = ["Laptop", "Mouse", "Keyboard"]

for item in products:
    print(item)



# Method 2
products = ["Laptop", "Mouse", "Keyboard"]

iterator = iter(products)

while True:
    try:
        item = next(iterator) 
        print(item)

    except StopIteration:
        break

# products
#    ↓
# iter(products)
#    ↓
# iterator
#    ↓
# next() → Laptop
# next() → Mouse
# next() → Keyboard
# next() → StopIteration
#    ↓
# break