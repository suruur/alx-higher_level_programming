#!/usr/bin/python3

def uppercase(s):

    for char in s:
        if 'a' <= char <= 'z':
            upper_chr = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(upper_chr), end = '')
        else:
            print("{}".format(char), end = '')
    print()
