#!/usr/bin/python3
"""
python script that featches a particular url
"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

with urllib.request.urlopen(url) as response:
    data = response.read()
    data_format = data.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data_format))
