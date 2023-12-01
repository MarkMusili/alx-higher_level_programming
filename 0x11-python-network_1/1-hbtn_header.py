#!/usr/bin/python3
"""Requests the header from a url"""
import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
	header_info = response.headers.get("X-Request-Id")

if __name__ == "__main__":
	print(header_info)
