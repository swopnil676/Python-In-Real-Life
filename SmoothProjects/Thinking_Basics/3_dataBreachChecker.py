import requests

email = "swopnilbiswas186@gmail.com"
url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
headers = {"hibp-api-key": "YOUR_KEY"}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    print("EMAIL WAS HACKED!")
else:
    print("Email is Safe!")