#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if len(my_list) == 0:
        return 0
    else:
        idx = -1
        for i in my_list:
            print("{}".format(my_list[idx]))
            idx += -1
