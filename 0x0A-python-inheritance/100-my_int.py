#!/usr/bin/python3

"""
12. My integer: handling eq and ne methods
"""


class MyInt(int):
    """
    a child class of int that has inverted operatores

    Returns:
        inverted == and != signs

    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
