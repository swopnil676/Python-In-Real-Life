import webbrowser
import time

print("__INITIALIZING MY WORKSPACE__")
time.sleep(1)

# sites = ["youtube.com"] 
sites = ["google.com"] 

for site in sites:
    print(f">>Opening:{site}")
    webbrowser.open(f"https://{site}")
    time.sleep(1)

print("\nWorkspace Ready. Now hustle!")
