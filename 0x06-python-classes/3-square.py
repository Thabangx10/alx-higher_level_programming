#!/usr/bin/python3

"""documentation of the module."""

class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError('size must be integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Public instance method: def area(self): that returns the current square."""
        return (self.__size * self.__size)
