#!/usr/bin/python3
"""
7. Error code #1
"""
import requests
import sys

url = sys.argv[1]

req = requests.get(url)
print(req.text)

if req.status_code >= 400:
    print(f"Error code: {req.status_code}")
