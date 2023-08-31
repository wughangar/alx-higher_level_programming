#!/usr/bin/python3

"""
4. Only sub class of
"""


def inherits_from(obj, a_class):
    """
    function that checks if an object is an instance of a subclass

    Args:
        obj: onject to be checked
        a_class: class the object is checked in

    Returns:
        True: if an object has directly inheritaed from said class
        False: if otherwise
    """

    return isinstance(obj, a_class) and type(obj) != a_class
