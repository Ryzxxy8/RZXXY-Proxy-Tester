import sys
import unittest
from pathlib import Path
from urllib.parse import quote
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import proxy_config

class TestProxyConfig(unittest.TestCase):
    def setUp(self):
        self.original = {name: getattr(proxy_config, name) for name in ["PROXY_ENABLED", "PROXY_HOST", "PROXY_PORT", "PROXY_USERNAME", "PROXY_PASSWORD"]}
    def tearDown(self):
        for name, value in self.original.items():
            setattr(proxy_config, name, value)
    def test_proxy_disabled(self):
        proxy_config.PROXY_ENABLED = False
        self.assertIsNone(proxy_config.get_proxy_url())
    def test_missing_host(self):
        proxy_config.PROXY_ENABLED = True
        proxy_config.PROXY_HOST = ""
        proxy_config.PROXY_PORT = "8080"
        self.assertIsNone(proxy_config.get_proxy_url())
    def test_proxy_without_auth(self):
        proxy_config.PROXY_ENABLED = True
        proxy_config.PROXY_HOST = "127.0.0.1"
        proxy_config.PROXY_PORT = "8080"
        proxy_config.PROXY_USERNAME = ""
        proxy_config.PROXY_PASSWORD = ""
        self.assertEqual(proxy_config.get_proxy_url(), "http://127.0.0.1:8080")
    def test_credentials_are_encoded(self):
        proxy_config.PROXY_ENABLED = True
        proxy_config.PROXY_HOST = "127.0.0.1"
        proxy_config.PROXY_PORT = "8080"
        proxy_config.PROXY_USERNAME = "user@name"
        proxy_config.PROXY_PASSWORD = "pass:word"
        expected = "http://" + quote("user@name", safe="") + ":" + quote("pass:word", safe="") + "@127.0.0.1:8080"
        self.assertEqual(proxy_config.get_proxy_url(), expected)

if __name__ == "__main__":
    unittest.main()
