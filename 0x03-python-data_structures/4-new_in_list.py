#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    if idx < 0:
        return my_list.copy()
    elif idx >= len(my_list):
        return my_list.copy()
    else:
        new_list = my_list[:idx] + [element] + [idx + 1:]

    return new_list
