text = input("Enter Your Message: ")

secret_code = "".join([chr(ord(c)+1) for c in text])
print(f"\n>> Encoded Message: {secret_code}")
print("Your privacy is protected by python")