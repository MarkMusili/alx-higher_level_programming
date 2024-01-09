#!/usr/bin/python3
"""Post a variable to intiate a serach"""
import requests
import sys


if __name__ == "__main__":
    url_d = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if sys.argv else ""
    r = requests.post(url=url_d, data={'q': q})
    try:
        found = r.json()

        if found:
            print(f"[{found.get('id')}] {found.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("None")
