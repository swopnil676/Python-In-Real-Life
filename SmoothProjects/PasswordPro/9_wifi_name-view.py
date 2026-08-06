import subprocess

# Get WiFi profiles
profiles = subprocess.check_output(
    "netsh wlan show profiles",
    shell=True
).decode(errors="ignore")

# Extract names
names = []

for line in profiles.split("\n"):
    if "All User Profile" in line:
        names.append(line.split(":")[1].strip())

# Print profiles
for i, n in enumerate(names, 1):
    print(f"[{i}] {n}")

# User choice
ch = int(input("\nChoose WiFi number: "))

# Check valid choice
if ch < 1 or ch > len(names):
    print("Invalid number!")
    exit()

wifi = names[ch - 1]

try:
    # Get password
    result = subprocess.check_output(
        f'netsh wlan show profile "{wifi}" key=clear',
        shell=True
    ).decode(errors="ignore")

    print(result)

except subprocess.CalledProcessError:
    print(f"\nCannot access WiFi profile: {wifi}")