#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if len(my_list) == 0:
        return 0
    if idx < 0 or idx >= len(my_list):
        return my_list
    if len(my_list) != 1:
        my_list = my_list[:idx] + my_list[idx + 1:]
    else:
        my_list = []

    return my_list
