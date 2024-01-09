#!/usr/bin/python3
"""Make a POST request to the server"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode("utf-8")

    request_url = urllib.request.Request(url=url, data=data, method="POST")

    with urllib.request.urlopen(request_url) as response:
        response_email = response.read().decode("utf-8")

    print(response_email)
