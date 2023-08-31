#!/usr/bin/python3
"""
0. Lookup
"""


def lookup(obj):
    """
    function that returns a list of available attributes and methods

    Args:
        obj: object to be checked

    Returns:
        a list
    """
    return dir(obj)
