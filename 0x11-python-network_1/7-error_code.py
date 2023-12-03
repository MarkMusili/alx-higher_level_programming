#!/usr/bin/python3
"""Post a variable"""
import requests
import sys


url = sys.argv[1]
r = requests.get(url)

if __name__ == "__main__":
    print(f"Error code: {r.status_code}")
