#!/usr/bin/python3
"""defines Student
"""


class Student:
    """Contains Student data
    """

    def __init__(self, first_name, last_name, age):
        """Initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Retrives data with some added filter
        """

        if attr == None or type(attr) != list:
            return self.__dict__
        else:
            temp = {}
            for elem in attr:
                if type(elem) != str:
                    return self.__dict__
                if elem in self.__dict__.keys():
                    temp[elem] = self.__dict__[elem]
            return temp
