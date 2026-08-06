import subprocess

# Get saved WiFi profiles
profiles = subprocess.check_output(
    "netsh wlan show profiles",
    shell=True
).decode()

# Extract WiFi names
names = [
    line.split(":")[1].strip()
    for line in profiles.split("\n")
    if "All User Profile" in line
]

# Show list
for i, n in enumerate(names, 1):
    print(f"[{i}] {n}")

# Choose WiFi
ch = int(input("\nChoose WiFi number: "))
wifi = names[ch - 1]

# Get password
result = subprocess.check_output(
    f'netsh wlan show profile "{wifi}" key=clear',
    shell=True
).decode()

print("\n" + result)