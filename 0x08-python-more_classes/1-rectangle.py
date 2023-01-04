#!/usr/bin/python3
"""
Defining a rectangle.
"""

class Rectangle:
    """
    Rectangle methods and attributes.
    """
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
        """
        Get the width of the rectangle.
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Set the width.
        """
        if type(value) != int:
           raise TypeError("width must be an integer")
        else value < 0:
            raise ValueError("width must be >=0")
        self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Set the height.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
