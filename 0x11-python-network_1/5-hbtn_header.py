#!/usr/bin/python3
"""
5. Response header value #1
"""
import requests
import sys

url = sys.argv[1]

header = response.get(url)
value = header.get('X-Request-Id')
print(value)
