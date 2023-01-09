#!/usr/bin/python3
"""is_kind_class
"""

def is_kind_class(obj, a_class):
    """ Function:
                 returns 'TRUE', if obj isinstance of the class 
                 or the inherited obj instance from class

                 Otherwise return 'FALSE'
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
