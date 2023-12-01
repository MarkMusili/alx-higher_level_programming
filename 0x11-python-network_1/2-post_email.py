#!/usr/bin/python3
"""Make a POST request to the server"""
import sys
import request
import parse


url = sys.argv[1]
email = sys.argv[2]

data = parse.urlencode({'email': email}).encode("utf-8")

request_url = request.Request(url=url, data=data, method="POST")

with request.urlopen(request_url) as response:
    response_email = response.read().decode("utf-8")

if __name__ == "__main__":
    print(response_email)
