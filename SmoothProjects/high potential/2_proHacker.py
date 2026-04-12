import os
import time
import random

# Clear screen (works on Windows/Linux)
os.system("cls" if os.name == "nt" else "clear")

# Hacker steps (fixed commas + improved text)
lines = [
    "[+] Connecting to secure server...",
    "[+] Bypassing firewall...",
    "[+] Injecting payload...",
    "[+] Accessing database...",
    "[+] Decrypting passwords...",
    "[+] Uploading virus...",
    "[+] System control acquired!",
    "[✓] HACK COMPLETE"
]

# Number rain effect
print("\033[92m")  # Green color
for i in range(50):
    print(" ".join(str(random.randint(100000, 999999)) for _ in range(6)))
    time.sleep(0.05)

print("\033[0m")

# Typing effect function
def type_text(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()

# Show hacking steps
for line in lines:
    print("\033[96m", end="")  # Cyan color
    type_text(line)
    time.sleep(0.4)

# Fake progress
print("\n\033[93mProcessing:\033[0m")
for i in range(0, 101, 5):
    bar = "█" * (i // 5) + "-" * (20 - i // 5)
    print(f"\r[{bar}] {i}%", end="")
    time.sleep(0.1)

print("\n")

# Final warning (red scary text)
print("\033[91m")
type_text(">>> WARNING: SYSTEM BREACH DETECTED <<<")
type_text(">>> YOU ARE BEING WATCHED <<<")
type_text(">>> ACCESSING PERSONAL FILES <<<")
print("\033[0m")

# Fake IP tracking
time.sleep(1)
print("\033[93mTracking IP...\033[0m")
time.sleep(1)

fake_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
print(f"\033[92m[+] IP FOUND: {fake_ip}\033[0m")

print("\n\033[92mMission Complete ✔\033[0m")