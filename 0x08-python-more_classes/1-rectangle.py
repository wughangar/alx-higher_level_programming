#!/usr/bin/python3

"""
1. Real definition of a rectangle
"""


class Rectangle:
    """
    class that defines Rectangle width and height
    """
    def __init__(self, width=0, height=0):
        """
        initializes the rectangle width and height to zero

        Args:
        width: the width of the rectangle
        height: the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        gets width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width to value

        Args:
        value: to be set to width

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an inetger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):

        """
        sets the height to value

        Args:
        value: to be set to height and must be an int and > 0

        Raises:
            TypeError: when height is not an integer
            ValueError:  when height is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
