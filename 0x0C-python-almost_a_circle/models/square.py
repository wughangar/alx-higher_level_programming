#!/usr/bin/python3

"""
10. And now, the Square!
"""
from rectangle import Rectangle


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
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """
        sets the value if size fo width and height
        """
        self._Rectangle__width = value
        self._Rectangle__height = value

    def __str__(self):
        """
        returns a string
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def width(self):
        """
        getter for width
        """
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """
        sets width to value

        Raises:
            TypeError: when width is not an integer
            ValueError: when value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value
        self._Rectangle__height = value

    @property
    def height(self):
        """
        height setter
        """
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """
        sets the height to value

        Raises:
            TypeError: when height is not an integer
            ValueError: when value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("value must be >=  0")
        self._Rectangle__height = value
        self._Rectangle__width = value

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
