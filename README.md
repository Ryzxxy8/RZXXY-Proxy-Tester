# RZXXY Proxy Tester

A lightweight Python tool for testing internet connectivity and HTTP proxy configuration.

## Features
- Check internet connectivity
- Display public IP information
- Check HTTP response status
- Enable or disable proxy configuration
- Read proxy settings from environment variables
- Configurable request timeout

## Requirements
- Python 3.13+
- requests library

## Installation
python3 -m pip install requests

## Run
python3 src/proxy_checker.py

## Configuration
Proxy is disabled by default. Configure these environment variables when using an authorized HTTP proxy:
- PROXY_ENABLED
- PROXY_HOST
- PROXY_PORT
- PROXY_USERNAME (optional)
- PROXY_PASSWORD (optional)

Never commit proxy credentials or .env files to GitHub.

## Project Structure
```
RZXXY-Proxy-Tester/
├── src/
│   ├── proxy_config.py
│   └── proxy_checker.py
├── tests/
├── .gitignore
└── README.md
```

## Project Status
Development in progress.

## Developer
RZXXY
