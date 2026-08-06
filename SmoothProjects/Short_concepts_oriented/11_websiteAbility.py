# Method 1
# import socket

# sites = ["twitter.com", "facebook.com"]

# for site in sites:
#     try:
#         socket.gethostbyname(site)
#         print(f"{site} is ONLINE")
#     except:
#         print(f"{site} is DOWN")


# Method 2
import requests

try:
    response = requests.get("https://google.com", timeout=5)

    if response.status_code == 200:
        print("Website is up")
    else:
        print("Website responded with:", response.status_code)

except requests.exceptions.RequestException:
    print("Website is down")