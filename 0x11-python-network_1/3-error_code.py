#!/usr/bin/python3
"""Handle HTTP errors"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    request_url = urllib.request.Request(url)
    try:
        urllib.request.urlopen(request_url)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
