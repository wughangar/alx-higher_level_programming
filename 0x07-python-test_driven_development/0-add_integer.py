#!/usr/bin/python3

"""
Question 0: adds 2 integers
"""

def add_integer(a, b=98):
    """
    adds two integers.

    Args:
        a: first number- if its a float- will be converted to an int
        b: second number and if its a flaot, it will be converted to int

    Returns:
        int: the sum of a and b

    Raises:
       TypeError; if a or b are not integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
