#!/usr/bin/python3
"""
2. POST an email #0
"""

import urllib.request
import sys

url = sys.argv[1]
data = sys.argv[2]

req =  urllib.request.Request(url, data=data, method="POST")
with urllib.request.urlopen(req) as response:
    ans = response.read()
    decorded_ans = ans.decord('utf-8')
    print(decorded_ans)
