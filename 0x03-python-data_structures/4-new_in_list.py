#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    new_list = my_list
    if idx < 0:
        return new_list
    elif idx >= len(my_list):
        return new_list
    elif len(my_list) == 1:
        new_list[idx] = element
    else:
        new_list = my_list[:idx] + [element] + [idx + 1:]

    return new_list
