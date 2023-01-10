#!/usr/bin/python3
"""Writing to a file 
"""

def number_of_lines(filename="", text=""):
    """
    You must use the with statement

    You don’t need to manage file permission exceptions.

    Your function should create the file if doesn’t exist.

    Your function should overwrite the content of the file if it already exists.
    """

    with open(filename, encoding="utf-8") as readFile:
        lines = 0
        while True:
            line = readFile.readline()
            if not line:
                break
            lines += 1
        return lines
