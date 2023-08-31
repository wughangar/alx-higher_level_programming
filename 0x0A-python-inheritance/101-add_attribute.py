#!/usr/bin/python3
"""
13. Can I? : sets attribute and raises error if it cant
"""


def add_attribute(obj, attr, value):
    """
    function that adds attribute or raises error if it cant

    Args:
        obj: objet to have attrivute added to
        attr: attribute to be added
        value: value of the attribute

    Raises:
        TypeError: when attribute cant be added
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
