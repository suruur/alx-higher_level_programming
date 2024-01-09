#!/usr/bin/python3

def append_write(filename="", text=""):

    with open(filename, 'a', encoding='utf-8') as file:
        no_ofchars = file.write(text)
    return no_ofchars
