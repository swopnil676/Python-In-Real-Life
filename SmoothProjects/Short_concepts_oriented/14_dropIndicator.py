import time
import requests

drops, total = 0, 10

for _ in range(total):
    t0 = time.time()
    try:
        # Check latency against Google with a strict 0.5s timeout
        requests.get("https://google.com", timeout=0.5)
    except:
        drops += 1
        
    print("Ping:", (time.time() - t0) * 1000)

print("Drops:", drops, "/", total)