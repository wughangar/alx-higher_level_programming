#!/usr/bin/python3
"""
6. Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    function that creates an object from json file

    Args:
        filename: file to store the object file

    """
    with open(filename, "r") as f:
        return json.load(f)
