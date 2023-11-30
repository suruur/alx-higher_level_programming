#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    print(f"{argc} argument{'s' if argc != 1 else ''}\
            {'.' if argc == 0 else ':'}")

    for i, arg in enumerate(argv, start=1):
        print(f"{i}: {arg}")
