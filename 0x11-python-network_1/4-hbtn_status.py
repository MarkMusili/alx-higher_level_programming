#!/usr/bin/python3
"""Use the request package"""
import requests

url = "https://alx-intranet.hbtn.io/status"
response = requests.get(url)

if __name__ == "__main__":
	print("Body response:")
	print(f"	- type: {type(response.text)}")
	print(f"	- content: {response.text}")