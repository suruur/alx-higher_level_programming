#!/usr/bin/python3
def no_c(my_string):

    if __name__ == "__main__":
        res = ""
        for char in my_string:
            if char.lower() != 'c' or char.upper() != 'C':
                res += char

        return (res)
