import os
from urllib.parse import quote

PROXY_ENABLED = os.getenv("PROXY_ENABLED", "false").lower() == "true"
PROXY_HOST = os.getenv("PROXY_HOST", "")
PROXY_PORT = os.getenv("PROXY_PORT", "")
PROXY_USERNAME = os.getenv("PROXY_USERNAME", "")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD", "")
TIMEOUT = 15
TEST_URL = "https://httpbin.org/ip"

def get_proxy_url():
    if not PROXY_ENABLED or not PROXY_HOST or not PROXY_PORT:
        return None
    if PROXY_USERNAME and PROXY_PASSWORD:
        username = quote(PROXY_USERNAME, safe="")
        password = quote(PROXY_PASSWORD, safe="")
        return f"http://{username}:{password}@{PROXY_HOST}:{PROXY_PORT}"
    return f"http://{PROXY_HOST}:{PROXY_PORT}"
