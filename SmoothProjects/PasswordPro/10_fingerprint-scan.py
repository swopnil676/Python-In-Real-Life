import time

print("""
╔══════════════════╗
║ FINGERPRINT SCAN ║
╚══════════════════╝
""")

input("Place Finger And Press Enter...:")

steps = ["scanning..!",
         "Reading Biometrics...!",
         "Matching Identity",
         "Unlcoking System"]

for step in steps:
    print(step)
    time.sleep(0.5)

print("\nACCESS GRANTED ✅")