#!/usr/bin/python3
"""rectangle class that inherits from base
"""

from model.base import Base


class Rectangle(Base):
    """Inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width
        """
        return self.__width

    @width.setter
    def width(width, value):
        if type(value) != int:
            raise TypeError("width is not a integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("X must be an integer")
        if value <= 0:
            raise ValueError("X must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("Y must be an integer")
        if value <= 0:
            raise ValueError("Y must be > 0")

    def area(self):
        """Returns the area
        """
        return self.width * self.height

    def display(self):
        """Return the ouput of the shape with '#'
           characters.
           
           y = is the newline
           x = is the space
        """
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """Formatted display
        """
        return "[{}] ({}) {}/{} - {}/{}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width, self.height)

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        """Internal method that updates instance attributes via */**args."""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """Updates instance attributes via no-keyword & keyword args."""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of this class."""
        return {"id": self.id, "width": self.__width, "height": self.__height,"x": self.__x, "y": self.__y}
