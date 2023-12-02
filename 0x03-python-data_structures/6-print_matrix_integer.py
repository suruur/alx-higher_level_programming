#!/usr/bin/python3
def print_matrix_integer(matrix):

    if __name__ == "__main__":
        for row in matrix:
            for element in row:
                print("{:d}".format(element), end=" " if element != row[-1] else "")
            print();

