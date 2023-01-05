#!/usr/bin/python3
"""Defining the locked class"""

class LockedClass:
    """
    Preventing the user from instantiating any new atrributes
    except for onrs called 'first_name'.
    """

    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + attribute + "'")
