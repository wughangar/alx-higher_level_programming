#!/usr/bin/python3
"""
question 2: size validation
"""


class Square:
    """
    class that defines a square
    """

    def __init__(self, size=0):
        """
        validates a square instance size.

        Args:
        size: private instance attribute of the square initialized to zero

        Raises:
            TypeError: raises if size is not an integer
            ValueError: Raised if the size if less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
