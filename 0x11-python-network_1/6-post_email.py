#!/usr/bin/python3
"""Post a variable"""
import requests
import sys


url = sys.argv[1]
email = sys.argv[2]
r = requests.post(url, data={'email': email})

if __name__ == "__main__":
    print(r.text)
