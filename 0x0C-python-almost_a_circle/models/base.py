#!/usr/bin/python3

"""
1. Base class
"""


class Base:
    """
    base class for other classes in the project
    This class has a private class attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        class constructor
        Args:
           id: to be asigned to the private attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
