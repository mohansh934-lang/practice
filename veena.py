import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "https://api.audius.co/v1/tracks/search"
PARAMS = {
    "query": "Arijit Singh",
    "limit": 10
}

def test(i):
    start = time.perf_counter()
    try:
        r = requests.get(URL, params=PARAMS, timeout=10)
        elapsed = time.perf_counter() - start
        return i, r.status_code, elapsed
    except Exception as e:
        return i, "ERROR", str(e)

TOTAL = 10

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=10) as pool:
    futures = [pool.submit(test, i) for i in range(TOTAL)]

    for f in as_completed(futures):
        i, status, elapsed = f.result()
        print(f"{i:02d} | {status} | {elapsed:.3f}s")

total_time = time.perf_counter() - start

print("\n----------------------")
print(f"Total requests : {TOTAL}")
print(f"Total time     : {total_time:.3f}s")
print(f"Requests/sec   : {TOTAL / total_time:.2f}")
print("----------------------")