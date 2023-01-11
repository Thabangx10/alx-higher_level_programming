#!/usr/bin/python3
"""Inherits from 'RECTANGLE' which also hail from 'BaseGeometry'
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Data from 'Rectangle
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of square
        """

        return self.__size * self.__size

    def __str__(self):
        """Magic method for description
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
