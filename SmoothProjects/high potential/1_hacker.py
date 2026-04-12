import os
import time
import random

os.system("cls" if os.name == "nt" else "clear")    # windows clear screen

lines = [
"[+] connecting to secure server...",
"[+] Bypassing firewall...",
"[+] Injecting payload...",
"[+] Accessing database...",
"[+] Descripting password...",
"[+] Uploading virus...",
"[+] system control acquired!",
"[✔️] HACK COMPLETE "
]

# Random numbers
for i in range(100):
    print(f"{random.randint(100000,999999)}")
    time.sleep(0.05)

# Show steps
for line in lines:
    print(line)
    time.sleep(0.4)

# Final message
print("\n\033[91m>>> YOU ARE BEING WATCHED AND HACKED!! <<<\033[0m")