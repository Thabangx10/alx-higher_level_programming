#!/usr/bin/python3

""" size must be an integer, otherwise raise a TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError exception with the message size must be >= 0

Public instance method: def area(self): that returns the current square area"""

class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        size = self.__size
        return size * size
