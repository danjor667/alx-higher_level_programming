#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list:
        up = 0
        down = 0
        for key, value in dict(my_list).items():
            up += (key * value)
            down += value
        return up / down
    else:
        return 0
