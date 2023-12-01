#!/usr/bin/python3
"""Requests the header from a url"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_info = response.headers.get("X-Request-Id")
    print(header_info)

