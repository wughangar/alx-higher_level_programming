#!/usr/bin/python3
"""
script that takes a url and catches the urllib.error.HTTPError
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            print(data)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e}")
