import secrets
import string

print("=== Secure Password Generator ===")

# 🔹 User input
length = int(input("Enter password length: "))

use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

# 🔹 Build character pool
alphabet = ""
password = []

if use_lower:
    alphabet += string.ascii_lowercase
    password.append(secrets.choice(string.ascii_lowercase))

if use_upper:
    alphabet += string.ascii_uppercase
    password.append(secrets.choice(string.ascii_uppercase))

if use_digits:
    alphabet += string.digits
    password.append(secrets.choice(string.digits))

if use_symbols:
    alphabet += string.punctuation
    password.append(secrets.choice(string.punctuation))

# ❌ Validation
if not alphabet:
    print("You must select at least one character type!")
    exit()

if length < len(password):
    print("Length too short for selected options!")
    exit()

# 🔹 Fill remaining length
for _ in range(length - len(password)):
    password.append(secrets.choice(alphabet))

# 🔹 Shuffle
secrets.SystemRandom().shuffle(password)

# 🔹 Final password
password = ''.join(password)

print("\nGenerated Password:", password)