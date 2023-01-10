#!/usr/bin/python3
"""inherits_from
"""


def inherits_from(obj, a_class):
    """Function:
               Returns 'True', if obj has been directly inherited
               as an instance of a class.

               Otherwise return 'False'
    """
    if type(obj) is a_class or not isinstance(obj, a_class):
        return False
    else:
        return True
