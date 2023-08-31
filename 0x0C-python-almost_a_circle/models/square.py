#!/usr/bin/python3

"""
10. And now, the Square!
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class that inherits all methods from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        square class constructor

        Args:
            size : size of the square
            x and y : cordinates for the position of the square
            id: keeps count of the number of objects
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size setter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        sets the value if size fo width and height
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        returns a string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        getter for width
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter method for size (width or height).

        Args:
           value: value to set for size(width and height)
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        function that updates attributes using key and value system

        Args:
           args: assigns attributes to args
           kwargs: updates key values args to attributes
        """
        if args:
            attr = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], arg)

        if kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        returns a dictionary rep of the square
        """
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
