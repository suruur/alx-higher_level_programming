#!/usr/bin/python3
def no_c(my_string):

    res = ""
    for char in my_string:
        if char.lower() != 'c' or char.upper() != 'C':
            res += char

    return (res)
