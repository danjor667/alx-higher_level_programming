#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    for ele in my_list[::-1]:
            print("{:d}".format(ele))




list = [1, 2, 3, 4, 5]

print_reversed_list_integer(list)
