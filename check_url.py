import requests
from tqdm import tqdm


def check_urls():
    with open('url.txt', 'r') as f1:
        urls = f1.readlines()
    with open('url_live.txt', 'w') as f2:
        for url in tqdm(urls, desc='Checking URLs'):
            url = url.strip()
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    f2.write(url + '\n')
                    f2.flush()
                    print(url + ' live!')
            except requests.exceptions.Timeout:
                print(f"Timeout while checking {url}.")
            except:
                pass

check_urls()
