#!/usr/bin/python3
"""is_kind_class, uses a class checking function
"""

def is_kind_class(obj, a_class):
    """Returns 'TRUE', if obj isinstance of the class 
    or the inherited obj instance from class. Otherwise return 'FALSE'
        
    Parameters:
            obj (any) - check the object
            a_class (type) - the class to math the the type of 'obj' to.
    """

    if isinstance(obj, a_class):
        return True
    return False
