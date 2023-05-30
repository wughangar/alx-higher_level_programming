#!/usr/bin/python3


class Square:
    """
    A class that defines a square
    size: private instance attribute shown by __size
    Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """
        Initializing a square instance
        Args:
            size: square length on each side
        """
        self.__size = size
