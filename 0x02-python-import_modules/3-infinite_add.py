#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    arg_sum = 0

    for arg in argv:
        arg_sum += int(arg)
    print("{}".format(arg_sum))
