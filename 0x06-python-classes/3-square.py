#!/usr/bin/python3
"""
question 3: area of a square
"""


class Square:
    """
    class that defines a square
    """

    def __init__(self, size=0):
        """
        initializes a square instance size to zero.

        Args:
        size: size of a square

        Raises:
        TypeError: if size is not an integer
        ValueError: is size if less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        calculates the area of this sqaure

        Returns:
            float: Square area
        """
        return self.__size ** 2
