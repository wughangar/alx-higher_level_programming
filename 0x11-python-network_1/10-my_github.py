#!/usr/bin/python3
"""
9. My GitHub!
"""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    auth = HTTPBasicAuth(username, token)
    response = requests.get('https://api.github.com/user', auth=auth)
    print(response.json().get('id'))
