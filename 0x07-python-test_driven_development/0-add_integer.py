#!/usr/bin/python3
"""
add_integer:
    Checks if the parameters are(int) datatypes
    Return a sum
"""


def add_integer(a, b=98):
    """
    check if data is int.
    """
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != int:
        raise TypeError("b must an integer")
    else:
        return a + b
