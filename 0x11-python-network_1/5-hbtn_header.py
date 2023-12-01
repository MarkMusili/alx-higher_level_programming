#!/usr/bin/python3
"""Get a specific value from the response"""
import requests
import sys


url = sys.argv[1]
response = requests.get(url)
value = response.headers.get("X-Request-Id")

if __name__ == "__main__":
    print(value)
