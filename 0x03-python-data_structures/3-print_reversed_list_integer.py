#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if my_list == None:
        return 0
    if len(my_list) == 0:
        return 0
    elif len(my_list) == 1:
        print("{:d}".format(my_list[0]))
    else:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
