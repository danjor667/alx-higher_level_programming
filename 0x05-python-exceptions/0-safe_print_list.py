#!/usr/bin/env bash

def safe_print_list(my_list=[], x=0):
    n = 0
    for i < x:
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
        n += 1
    print("")
    return (n)
