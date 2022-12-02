#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list """We return the original list"""
    else:
        my_list[idx] = element """Updateed list"""
        return my_list
