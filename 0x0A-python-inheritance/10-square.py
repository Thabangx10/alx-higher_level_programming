#!/usr/bin/python3
"""Defines the Rectangle subclass"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square functions"""

    def __init__(self, size):
        """The size of the new square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area of the square"""

        return self.__size * self.__size
