#!/usr/bin/python3

"""Defining the Rectangle class"""

class Rectangle:
    """Representation of the rectangle

    Attributes:
             number_of_instances(int): Rectangle instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the new rectangle

        Values:
               width = int(value)
               height = int(value)
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
        if type(value) != int:
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, values):
        """Set height"""
        if type(value) != int:
            raise TypeError("must be an integer")
        if value < 0:
            raise ValueError("must be >= 0")
        self.__height = value

    def area(self):
        """Get the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the rectangle in characters of '#'"""
        rect = []
        if self.__width == 0 or self.__height == 0:
            return rect

        for i in range(self.__height):
            if i == self.__height -1:
                rect += ('#' * self.__width)
            else:
                rect += (('#' * self.width) + '\n')
        return rect

    def __repr__(self):
        """eval() function to return the rectangle"""
        w = str(self.__width)
        h = str(self.__height)

        rect = "Rectangle(" + w + ", " + h + ")"
        return rect

    def __del__(self):
        """print message using del() function"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
