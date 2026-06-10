inv = ["Sword", None,None]

if all(inv):
    print('Inventory full!')
elif any(inv):
    print('Inventory has items')
else:
    print('Inventory empty')