#!/usr/bin/python3

""" property setter def size(self, value): to set it:

    size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

    if size is less than 0, raise a ValueError exception with the message size must be >= 0
    Public instance method: def area(self): that returns the current square area"""

class Square:
    def __init__(self, size=0):
        """Private instance attribute: size:"""
        self.__size = size

    @property
    def size(self):
        """property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Public instance method: def area(self): that returns the current square area"""
        return self.__size ** 2
