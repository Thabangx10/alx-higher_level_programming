#!/usr/bin/python3
"""Defining a rectangle"""


class Rectangle:
    """Rectangle functions

    Atrributes:
               public instances
               print_symbol: string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __int__(self, width=0, height=0):
        """Initialization
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the width"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__height = value

    def area(self):
        """Returning the area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Represent the rectangle with '#' characters"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """eval() method to return width and height"""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """increment instance when __del__ is called"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
