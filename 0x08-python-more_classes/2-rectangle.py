#!/usr/bin/python3

"""Defining a Rectangle"""

class Rectangle:
    """Repr of a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle

        Values:
              width = int(value)
              height = int =(value)
              area = int * int
              perimeter = ((int*2) + (int*2)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be < 0.")

    @property
    def height(self):
        """Get/Set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != 0:
            raise TypeError("height must an integer")
        if value < 0:
            raise ValueError("height must be < 0")

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
