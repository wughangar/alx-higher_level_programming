#!/usr/bin/python3

"""
4. From JSON string to Object
"""
import json


def from_json_string(my_str):
    """
    function that returns a python object from JSON

    Args:
        my_str: JSON object to be converted into python

    Returns:
        python object
    """
    result = json.loads(my_str)
    return result
