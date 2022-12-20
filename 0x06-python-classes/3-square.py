#!/usr/bin/python3

"""Square class"""

class Square:
    """Square methods"""
    def __init__(self, size=0):
        
        """size must be an integer, otherwise raise a TypeError exception with the messa           ge size must be an integer"""

        if type(size) != int:
            raise TypeError('size must be integer')

        """if size is less than 0, raise a ValueError exception with the message size mu           st be >= 0"""
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    """Public instance method: def area(self): that returns the current square area"""

    def area(self):
        size = self.__size
        return size * size
