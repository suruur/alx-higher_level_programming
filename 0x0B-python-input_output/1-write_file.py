#!/usr/bin/python3

def write_file(filename="", text=""):

    with open(filename, 'w', encoding='utf-8') as file:
        no_ofchars = file.write(text)
    return no_ofchars
