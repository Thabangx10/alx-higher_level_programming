#!/usr/bin/python3

"""Defining a Rectangle"""

class Rectangle:
    """Representation of the triangle"""
    def __init__(self, width=0, height=0):
        """Initializing the new rectangle

        Values:
               width = int(value)
               height = int(value)
               area = value * value
               perimeter = ((value * 2) + (value * 2))
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__height = value

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter"""
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """rectangle characters '#'"""
        rect = []
        if self.__width == 0 or self.__height == 0:
            return rect

        for i in range(self.height):
            if i == self.__height -1:
                rect += ('#' * self.__width)
            else:
                rect += (('#' * self.__width) + '\n')
        return rect

    def __repr__(self):
        """Represent the rectangle in '#'"""
        w = str(self.__width)
        h = str(self.__height)

        rect = "Rectangle(" + w + ", " + h + ")"
        return rect

    def __del__(self):
        """Print message"""
        print("Bye rectangle...")
