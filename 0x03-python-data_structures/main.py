#!/usr/bin/python3
print("Inside Main ...")
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ]
#idx = 3
#ele = 9
#n_list = new_in_list(my_list, idx, ele)
print_matrix_integer(matrix)
print("--")
print_matrix_integer()

#print(n_list)
#print(my_list)
