#!/usr/bin/python3
"""Get the Id using GitHub API to authenitcate and get info"""
import requests
import sys


if __name__ == "__main__":
    url_git = " https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url_git, auth=(username, password))

    hacked_info = r.json()
    id = hacked_info.get("id")
    print(id)
