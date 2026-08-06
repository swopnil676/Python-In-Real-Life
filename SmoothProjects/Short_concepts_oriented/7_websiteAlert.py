import requests
import time

url = "https://www.amazon.in/"

try:
    old = requests.get(url).text

    while True:
        try:
            new = requests.get(url).text

            if new != old:
                print("Website Changed!")
                old = new

            time.sleep(60)

        except requests.RequestException:
            print("Connection Error")
            time.sleep(60)

except requests.RequestException:
    print("Could not access website")