import secrets
import string

alphabet = string.ascii_letters + string.digits + string.punctuation
choice_password = "".join(secrets.choice(alphabet) for _ in range(20))
print(f"{choice_password = }")

words = ["correct","herse","battery","staple","cloud","river","tiger","flame"]
passphrase = '-'.join(secrets.choice(words) for _ in range(4))
print(f"{passphrase = }")