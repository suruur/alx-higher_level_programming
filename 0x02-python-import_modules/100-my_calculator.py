#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
argc = len(sys.argv)
if argc < 3:
    print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
    exit(1)

a = int(sys.argv[1])
op = sys.argv[2]
b = int(sys.argv[3])

if __name__ == "__main__":
    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Avaiable operators: +, -, * and /")
        exit(1)
