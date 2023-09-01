#!/usr/bin/python3
"""
script that takes in url and sends request and displays value
"""
import sys
import urllib.request

url = sys.argv[1]

if __name__ == '__main__':
    """
    main function
    """
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        value = headers.get('X-Request-Id')
        print(value)
