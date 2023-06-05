#!/usr/bin/python3

"""
3. String representation
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

    def area(self):
        """
        returns the area od the rectangle
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """
        returns the perimeter of the reactangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = (self.width + self.height) * 2
        return perimeter

    def __str__(self):
        """
        gives a string representation of the rectangle using #
        """
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(["#" * self.width] * self.height)

    def __repr__(self):
        """
        returns string rep of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        number of instances to be decremented during each instance
        and vice versa
        to be called when rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
