import requests
import random
import time

# Proxy list from your screenshot
proxy_list = [
    'http://103.174.123.5:8089',
    'http://91.147.42.50:3128',
    'http://178.92.72.165:8080',
    'http://45.76.104.147:40001',
    'http://43.162.83.26:3128',
    'http://178.92.72.78:8080',
    'http://154.201.127.230:8080',
    'http://207.246.98.83:40001',
    'http://43.165.191.196:1082',
    'http://136.232.116.2:48976',
    'http://77.239.108.71:80',
    'http://31.28.4.192:80',
    'http://24.173.217.114:55443',
    'http://198.111.166.184:80',
    'http://191.5.38.6:54121',
    'http://2.28.105.45:8888',
    'http://157.245.70.5:10000',
    'http://103.166.0.25:1111',
]

# Function to pick a random proxy for each request
def get_random_proxy():
    proxy = random.choice(proxy_list)
    return {'http': proxy, 'https': proxy}

target_url = 'https://httpbin.org/ip'

for i in range(10):  # Send 10 requests
    proxies = get_random_proxy()
    try:
        print(f"Request {i+1} using proxy: {proxies['http']}")
        response = requests.get(target_url, proxies=proxies, timeout=10)
        print("IP seen by server:", response.json())
        print("-" * 40)
    except Exception as e:
        print(f"Request {i+1} failed (proxy might be dead): {e}")
        print("-" * 40)
    
    time.sleep(1)  # Wait 1 second between requests
