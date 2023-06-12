#!/usr/bin/python3

"""
3. Same class or inherit from
"""


def is_kind_of_class(obj, a_class):
    """
    function that cecks if an object is an instance of a class

    Args:
        obj: object being checked
        a_class: class the object is being cheked in

    Returns:
        True: if object is an instance of names class
        False: otherwise
    """
    return isinstance(obj, a_class)
