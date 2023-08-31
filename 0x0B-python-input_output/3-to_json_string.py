#!/usr/bin/python3

"""
3. To JSON string
"""
import json


def to_json_string(my_obj):
    """
    function kthat retuns a JSON representation of an object

    Args:
        my_obj: object to be converted inot JSON

    Returns:
        JSON representaion of an object

    """

    return json.dumps(my_obj)
