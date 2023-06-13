#!/usr/bin/python3
import json
"""
5. Save Object to a file
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an object to a text file

    Args:
        my_obj: object to be written into text file
        filename: text file to be written into

    """
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
