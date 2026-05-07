import secrets, string

alphabet = string.ascii_letters + string.digits + string.punctuation

password = [
    secrets.choice(string.ascii_lowercase),
    secrets.choice(string.ascii_uppercase),
    secrets.choice(string.digits),
    secrets.choice(string.punctuation)
]

password += [secrets.choice(alphabet) for _ in range(16)]
secrets.SystemRandom().shuffle(password)

password = ''.join(password)
print(password)