#!/usr/bin/python3

def uppercase(s):

    for char in s:
        if 'a' <= char <= 'z':
            upper_chr = chr(ord(char) - ord('a') + ord('A'))
            print(upper_chr, end = '')
        else:
            print(char, end = '')
    print()

