#!/usr/bin/python3
"""adds a new attribute to an object if it’s possible
"""


def add_attribute(at_class, name, value):
        """Adds new attribute
        """

        cannot_add = {int, str, float, list, dict, tuple, frozenset, type, object}

        if type(at_class) in cannot_add:
            raise TypeError("can't add new atrribute")

        at_class.__setatrr__(name, value)
