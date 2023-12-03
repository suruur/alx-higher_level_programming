#!/usr/bin/python3
print("Inside Main ...")
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0,1,3,4,5,6]
list_res = divisible_by_2(my_list)


i = 0
while i < len(list_res):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_res[i] else "is not"))
    i += 1
