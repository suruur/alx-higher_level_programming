#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    if matrix == [[]]:
        print("$")
    else:
        for row in matrix:
            for element in row:
                print("{:d}".format(element), end=" " if element != row[-1] else "$")
            print()
#    if matrix:
#        for row in matrix:
#            for elem in row:
#                print("{}".format(elem, end=" " if elem != row[-1] else "$"))
