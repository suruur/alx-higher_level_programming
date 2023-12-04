#!/usr/bin/python3
print("Inside Main ...")
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [0,1,3,4,5,6]
idx = 3
ele = 9
n_list = new_in_list(my_list, idx, ele)


print(n_list)
print(my_list)
