#!/usr/bin/python3
"""Rectangle data inherits from the parent class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Inhertis from the parent.
    """

    def __init__(self, width, height):
        """function used to find the width and height of the
        rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
