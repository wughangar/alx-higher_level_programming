#!/usr/bin/python3
"""
2. POST an email #0
"""

import urllib.request
import sys

if __name__ == "__main__":
    """
    post an email
    """
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req) as response:
        ans = response.read()
        decoded_ans = ans.decord('utf-8')
        print(decoded_ans)
