#!/usr/bin/python3
"""
python script that featches a particular url
"""
import requests

url = 'https://alx-intranet.hbtn.io/status'

response = requests.get(url)
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
