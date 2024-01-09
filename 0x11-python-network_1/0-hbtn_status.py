#!/usr/bin/python3
"""This module fetches resources from a url"""
import urllib.request


url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    body = response.read()
    content = body.decode('utf-8')

if __name__ == "__main__":
    print("Body response:")
    print(f"	- type: {type(body)}")
    print(f"	- content: {body}")
    print(f"	- utf8 content: {content}")
