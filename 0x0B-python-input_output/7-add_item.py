#!/usr/bin/python3
import json
import sys
import importlib
import os
"""
import the files
"""
save = importlib.import_module("5-save_to_json_file")
load = importlib.import_module("6-load_from_json_file")

"""
set the file name
"""
filename = "add_item.json"
"""
load pre-existing the data inot a specific file
handle command line arguements
save the file
"""
if os.path.exists(filename):
    data = load.load_from_json_file(filename)
else:
    data = []

data.extend(sys.argv[1:])
save.save_to_json_file(data, "add_item.json")
