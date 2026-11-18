import requests
from proxy_config import get_proxy_url, TIMEOUT, TEST_URL, PROXY_ENABLED

def check_connection():
    print()
    print("=== RZXXY PROXY TESTER ===")
    proxy_url = get_proxy_url()
    proxies = {"http": proxy_url, "https": proxy_url} if proxy_url else None
    try:
        response = requests.get(TEST_URL, proxies=proxies, timeout=TIMEOUT)
        response.raise_for_status()
        print()
        print("[+] Connection Successful")
        print("[+] Public IP:", response.json().get("origin"))
        print("[+] Status:", response.status_code)
        print("[+] Proxy Enabled:", bool(proxy_url))
    except requests.exceptions.RequestException as error:
        print()
        print("[-] Connection Error:", type(error).__name__)

if __name__ == "__main__":
    check_connection()
