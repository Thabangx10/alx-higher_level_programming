#!/usr/bin/python3
def uniq_add(my_list=[]):
    result_list = []
    result = 0
    for i in my_list:
        if i not in result_list:
            result_list.append(i)
    for uniqs in result_list:
        result += uniqs
    return result
