import base64

def is_base64(s):
    try:
        return base64.b64encode(base64.b64decode(s)) == s.encode()
    except:
        return False

with open("can_u_find_me.txt", "r") as file:
    content = file.read()

words = content.split()

for w in words:
    if is_base64(w):
        print("Valid Base64:", w)

decoded = base64.b64decode("nA8QfKDh")
print(decoded)