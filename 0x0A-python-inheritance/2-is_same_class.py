#!/usr/bin/python3
"""
2. Exact same object
"""


def is_same_class(obj, a_class):
    """
    function tht cecks if object is exactly an instance of specified class

    Args:
        obj: object to be checked
        a_class: class to be checked

    Returns:
        True: if object is exactly an insatnce of specified class
        False: otherwise
    """
    return type(obj) is a_class
