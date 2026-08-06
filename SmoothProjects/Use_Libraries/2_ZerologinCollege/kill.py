# import base64

# with open("can_u_find_me.txt", "rb") as file:
#     encoded = base64.b64encode(file.read())

# decoded = base64.b64decode(encoded)

# with open("decoded.txt", "wb") as out:
#     out.write(decoded)

# print(encoded.decode("nA8QfKDh"))

import base64

def safe_decode(s):
    s += "=" * (-len(s) % 4)
    try:
        return base64.b64decode(s)
    except Exception as e:
        return f"Error: {e}"

print(safe_decode("nA8QfKDh"))