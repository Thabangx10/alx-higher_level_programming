#!/usr/bin/python3

"""Defining a rectangle."""

class rectangle(self):
    """Repr: a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle

        Value:
              width = int(value)
              height = int(value)
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """Get/Set the width of the rectangle"""
        return self.__width

    def width(self, value):
        if type(value) != int:
           raise TypeError("width must be an integer")
        else value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """Get/Set the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
