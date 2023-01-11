#!/usr/bin/python3
"""Student
"""


class Student:
    """Contains student data
    """

    def __init__(self, first_name, last_name, age):
        """Initialization
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Retrieves dictionary of students which are filtered
        """

        if attr == None or type(attr) != list:
            return self.__dict__
        else:
            temp = {}
            for elem in atrr:
                if type(elem) != str:
                    return self.__dict__
                if elem in self.__dict__.keys():
                    temp[elem] = self.__dict__[elem]
            return temp

    def reload_from_json(self, json):
        """Replace
        """

        for items in json.keys():
            self.__dict__ = json[items]
