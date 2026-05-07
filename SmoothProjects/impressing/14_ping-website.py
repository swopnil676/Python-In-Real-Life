# Check if a Webservice is Running

import requests
# pip install requests

def check_website_health(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return f"Website {url} is UP (Code: 200)"
        else:
            return f"Website {url} is DOWN (Status Code: {response.status_code})"

    except requests.RequestException:
        return f"Website {url} is UNREACHABLE"


# Examples
print(check_website_health("https://www.google.com"))
print(check_website_health("https://invalid-url-example.com"))