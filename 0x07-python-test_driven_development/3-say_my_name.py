#!/usr/bin/python3
"""
function that prints the names as requested
"""

def say_my_name(first_name, last_name=""):
    """
    Prints - My name is <first name> <last name>

    Args:
        first_name: First name as a string
        Last_name: last name as a string but not required

    Raises:
        TypeError: if first of last name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
