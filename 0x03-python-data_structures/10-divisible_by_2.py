#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    res = [num % 2 == 0 for num in my_list]
    return res
