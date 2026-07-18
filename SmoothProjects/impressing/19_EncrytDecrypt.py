# Caesar Cipher Encryption & Decryption
def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a') 
        # write as
            # if char.isupper():
            #   start = ord('A')
            # else:
            #   start = ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter Message: ")

try:
    key = int(input("Enter Key (number): "))
except ValueError:
    print("❌ Please enter a valid number!")
    exit()

encrypted = encrypt(message, key)
print("\nEncrypted:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted:", decrypted)


# Example:
# Enter Message: ABC@
# Enter Key (number): 3

# Encrypted: DEF@
# Decrypted: ABC@


'''
Main Idea

Encryption shifts letters forward.

Example (shift = 3):

A → D
B → E
C → F

To decrypt, we need to shift letters backward by the same amount.

D → A
E → B
F → C

'''