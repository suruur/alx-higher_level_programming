#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if len(my_list) == 0:
        return 0
    else:
        for i in range(len(my_list) -1, -1, -1):
            print("{}".format(my_list[i]))
