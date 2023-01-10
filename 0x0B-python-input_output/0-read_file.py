#!/usr/bin/python3
"""Read file
"""

def read_file(filename=""):
    """Takes in the 'str' filename to read it.
    """

    with open(filename, encoding="utf-8") as readFile:
        print(readFile.read(), end='')
