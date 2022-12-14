#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    num = 0
    length = []
    while num < list_length:
        try:
            result = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except TypeError:
            result = 0
            print("wrong type")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            num += 1
            length.append(result)
    return length
