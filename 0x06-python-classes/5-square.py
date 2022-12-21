#!/usr/bin/python3

"""Class Sqaure"""

class Square:
    """Square method"""
    def __init__(self, size=0):
        """size (int): The size of the new square."""
        self.__size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    #Setter modifies
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        size = self.__size

"""Public instance method: def my_print(self): that prints in stdout the square with the character #:
         if size is equal to 0, print an empty line""" 
        if size == 0:
            print()

        for row in range(size):
            print('#' *size)
