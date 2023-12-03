#!/usr/bin/python3
"""Post a variable"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)

    print(f"Error code: {r.status_code}")
