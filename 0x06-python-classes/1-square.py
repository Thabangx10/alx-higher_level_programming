#!/usr/bin/python3

"""we will be using __init__ method to assign the size value 
   as an attribute to self"""

class Square:
    """Square"""
    def __init__(self, size):
        """
        Parameters:
                   size (int): The size of the new square.
        """
        self.__size = size
