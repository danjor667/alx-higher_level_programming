#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if len(my_list) != 0:
        for ele in my_list[::-1]:
            print("{:d}".format(ele))
