#!/usr/bin/python3
"""a class Student that defines a student
"""


class Student:
    """Student data
    """

    def __init__(self, first_name, last_name, age):
        """Initialization of student data
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """__dict__
        """
        return self.__dict__
