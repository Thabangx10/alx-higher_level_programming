#!/usr/bin/python3

"""A module to find the maximum integer in the list"""

def max_integer(list=[]):
    """The function of this module is to find and return the maximum
       integer within the list.
       if the 'len(list)' of the list is empty, return None
    """
    if len(list) == 0:
        return None

    result = list[0]
    x = 1

    while x < len(list):
        if list[x] > result:
            result = list[x]
        x += 1
    return result
