#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    idx < 0 or idx >= len(my_list):
        return my_list

    new_l = []
    for i, item in enumerate(my_list):
        if i != idx:
            new_l.append(item)

    return new_l
