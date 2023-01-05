#!/usr/bin/python3
"""Defining of a rectangle"""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing your new rectangle

        Values:
               width = int(value)
               height = int(value)
               area = value + value
               perimeter = ((value * 2) + (value * 2))
               rect = the representation of a rectangle using '#'
               w = str(value)
               h = str(value)
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle"""
        return self.height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        """Returning the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returning the perimeter"""
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Representation if the rectangle in '#'"""
        rect = ""

        if self.__width == 0 or self.__height == 0:
            return rect

        for i in range(self.__height):
            if i == self.__height - 1:
                rect += ('#' * self.__width)
            else:
                rect += (('#' * self.__width) + '\n')
        return rect

    def __repr__(self):
        """eval() function to return the width and height"""
        w = str(self.__width)
        h = str(self.__height)

        rect = "Rectangle(" + w + ", " + h + ")"
        return rect
