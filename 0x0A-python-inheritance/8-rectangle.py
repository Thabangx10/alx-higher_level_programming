#!/usr/bin/python3
"""Rectangle data inherits from the parent class
"""

class(Rectangle(BaseGeometry)):
    """Inhertis from the parent.
    """

    def __intit__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
