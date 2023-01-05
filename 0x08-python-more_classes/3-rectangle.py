#!/usr/bin/python3
"""Defining a Rectangle"""


class Rectangle:
    """Rectangle functions and attributes."""

    def __int__(self, width=0, height=0):
        """Initializing a new rectangle

        Values:
              width = int(value)
              height = int(value)
              area = int(value) * int(value)
              perimeter = (int * 2) + (int * 2)
              rect = representation of the rectangle using '#'
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if type(value) != int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) != int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.height * 2))

    def __str__(self):
        """Repr the rectangle with '#' characters"""
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect

        for i in range(self.__height):
            if i == self.__height -1:
                rect += ('#' * self.width)
            else:
                rect += (('#' * self.width) +\n)
        return rect
