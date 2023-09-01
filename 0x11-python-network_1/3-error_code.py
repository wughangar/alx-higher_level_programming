#!/usr/bin/python3
"""
script that takes a url and catches the urllib.error.HTTPError
"""
import urllib.request
import urllib.error
import sys

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        data = response.read()
        decoded_data = data.decord('utf-8')
        print(decoded_data)
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
