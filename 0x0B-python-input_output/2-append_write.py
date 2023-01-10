#!/usr/bin/python3
"""read_lines
"""


def read_lines(filename="", text=""):
    """Takes in str filename to read, and n lines w/ int nb_lines
    """

    with open(filename,"a", encoding="utf-8") as readFile:
        return readFile.write(text)
