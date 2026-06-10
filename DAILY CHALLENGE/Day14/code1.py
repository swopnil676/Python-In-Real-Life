# inventory = {
#     "keyboard": 42,
#     "mouse": 19
# }
# print(inventory["monitor"]) # KeyError: 'monitor'



inventory = {
    "keyboard": 42,
    "mouse": 19
}
print(inventory.get("monitor","Not in stock"))