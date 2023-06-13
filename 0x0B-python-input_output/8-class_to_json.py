#!/usr/bin/python3

"""
8. Class to JSON
"""
import json


def class_to_json(obj):
    """
    function that returns a dictionary description of attributes

    Args:
        obj: an instance of a class

    Returns:
        dictionary description
    """
    jdict = {}

    for a in dir(obj):
        if a.startswith('__'):
            continue
        value = getattr(obj, a)
        jdict[a] = value
    return jdict
