#!/usr/bin/python3

"""
7. Integer validator
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
