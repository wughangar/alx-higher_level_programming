#!/usr/bin/python3
"""
2. First Rectangle
"""
from base import Base


class Rectangle(Base):
    """
    rectangle class that inherits from base
    private instances include:
        width
        height
        x
        y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor

        Args:
            width - width of the rectangle
            height - height of the reactangle
            x and y - hold the position of the rectangle
        each attribute has its own setter and getter
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        calculates the area

        Returns:
            result
        """
        return self.__width * self.__height

    def display(self):
        """
        displays a rectange in #
        """
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        overrides the __str__ method
        """
        return (f"[Rectangle] ({self.id})"
                f"{self.__x}/{self.__y} -"
                f"{self.__width} / {self.__height}")

    def update(self, *args, **kwargs):
        """
        function that assigns each arg to attribute

        Args:
            args: assigns attribute to args
            kwargs: assignes key value args to attributes
        """
        if args:
            self.id = args[0]
            args = args[1:]
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value

    def to_dictionary(self):
        """
        returns the dictionary rep of the rectangle
        """
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
