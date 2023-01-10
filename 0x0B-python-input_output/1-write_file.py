#!/usr/bin/python3
"""Writing to a file 
"""

def write_file(filename="", text=""):
    """Writing a str to UTF8 text file

    You must use the with statement

    You don’t need to manage file permission exceptions.

    Your function should create the file if doesn’t exist.

    Your function should overwrite the content of the file if it already exists.
    """

    with open(filename,"w", encoding="utf-8") as readFile:
        return readFile.write(text)
