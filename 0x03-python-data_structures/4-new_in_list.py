#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """ We are creating a copy of 'my_list' , for the new index element inserted"""
    copy = my_list.copy() 
    """ If idx is negative, the function should return a copy of the original list;
    If idx is out of range (> of number of element in my_list), the function should return a copy of the original list"""
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        copy[idx] = element
        return copy
