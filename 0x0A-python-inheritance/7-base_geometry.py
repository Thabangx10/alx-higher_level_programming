#!/usr/bin/python3
"""BaseGeometry
"""

class BaseGeometry:
    """Functions:
                 def area()
                 integer_validator
    """

    def area(self):
        """NOT IMPLEMENTED
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating the value
        """

        if type(value) != int:
            raise TypeError(name + " must be an integer")

        if value <= 0:
            raise ValueError(name + " must be greater than 0")
