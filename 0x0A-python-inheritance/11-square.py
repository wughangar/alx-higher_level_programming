#!/usr/bin/python3

"""
10. Square #1
"""


class BaseGeometry:
    """
    base class
    """
    def area(self):
        """
        instance method for area

        Raises:
            Exception with message- area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validates value

        Args:
            name: a string
            value: value to be validated

        Raises:
            TypeError: when value is not an int
            ValueError: when value is less than 0
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greator than 0")


class Rectangle(BaseGeometry):
    """
    child class with intitialize width and height
    """
    def __init__(self, width, height):
        """
        method initializing width and height

        Args:
            width: width of the rectagle
            height: height of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        calculates the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        method for return format
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    child class for rectangle
    """

    def __init__(self, size):
        """
        square class method with size instantiation

        Args:
            size: length of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        method for return format
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
