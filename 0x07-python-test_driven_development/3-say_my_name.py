#!/usr/bin/python3
"""
say_my_name:
    print out the parameters which are,
    to output a first_name and a last_name in (str) format
"""
def say_my_name(first_name, last_name=" "):
    """
    Prints "My name is <first name> <last name>"
    check if:
    parameters are in str format
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
