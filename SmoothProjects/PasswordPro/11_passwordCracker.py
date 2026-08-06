import hashlib

# Hash of the password we are trying to find (corresponds to "python123")
hashed = hashlib.md5("python123".encode()).hexdigest()

# Simple dictionary list to test against
wordlist = ["admin", "password", "python123", "12435"]

for word in wordlist:
    # Hash each word in the list and compare it to the target hash
    if hashlib.md5(word.encode()).hexdigest() == hashed:
        print(f"Password found: {word}")
        break