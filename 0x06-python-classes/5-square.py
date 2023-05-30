#!/usr/bin/python3
"""
question 4: Access and update private attribute
"""


class Square:
    """
    class that defines a square
    """

    def __init__(self, size=0):
        """
        initializes a sqaure instance size to zer.

        Args:
        size: size of a sqaure

        Raises:
        TypeError: if size if not an integer
        ValueError: if size if less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        getter which gets the size of the square

        Returns:
        an int: size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        sets the size of the square

        Args:
        value: size of the square

        Raises:
        TypeError: if value if not an integer
        ValueError: if value if less than zero
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculates the area of a square

        Returns:
        an int: area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints a square with hashtag character

        Returns:
        None
        """

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
