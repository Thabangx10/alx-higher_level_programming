#!/usr/bin/python3
"""Defining the locked class"""

class LockedClass:
    """
    Preventing the user from instantiating any new atrributes
    except for onrs called 'first_name'.
    """

    ___slots___ = ["first_name"]
