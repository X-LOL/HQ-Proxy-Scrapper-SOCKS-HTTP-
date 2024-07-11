try:
    import requests
except ImportError:
    import subprocess
    subprocess.run(['pip', 'install', 'requests'])
    import requests

try:
    import bs4
except ImportError:
    import subprocess
    subprocess.run(['pip', 'install', 'bs4'])
    import bs4




import requests
from bs4 import BeautifulSoup
import time


print(f"[X] CODED BY X - L O L")
print(f"[X] Scrapping Proxyies")
print(f"[X] Scrapping Will Work Every 2 Mins")

time.sleep(3)

while True:

 def scrape_proxies(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    proxies = []
    for row in soup.find_all('tr')[1:]:
        cols = row.find_all('td')
        if len(cols) > 6:
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            protocol = cols[4].text.strip()
            proxies.append(f"{protocol}://{ip}:{port}")
    
    with open(filename, 'w') as f:
        for proxy in proxies:
            f.write(proxy + '\n')
    
    print(f"Proxies saved to {filename}")

 http_url = "https://free-proxy-list.net/"
 http_filename = "http_proxies.txt"
 scrape_proxies(http_url, http_filename)

 socks4_url = "https://socks-proxy.net/"
 socks4_filename = "socks4_proxies.txt"
 scrape_proxies(socks4_url, socks4_filename)

 socks5_url = "https://socks5-proxy.net/"
 socks5_filename = "socks5_proxies.txt"
 scrape_proxies(socks5_url, socks5_filename)

 time.sleep(120)