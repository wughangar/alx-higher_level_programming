#!/usr/bin/python3
"""
6. POST an email #1 with requests
"""
import requests
import sys

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}

req = requests.post(url, json=data)

print(req.text)
