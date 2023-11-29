#!/usr/bin/python3

def uppercase(s):

    i = 0
    for char in s:
        if 'a' <= char <= 'z':
            upper_chr = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(upper_chr), end='' if i < len(s) - 1 else '\n')
        else:
            print("{}".format(char), end=''\
                    if i < len(s) - 1 and s != "" else '\n')
        i = i + 1
