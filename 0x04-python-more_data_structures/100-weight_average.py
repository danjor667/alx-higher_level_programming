#!/usr/bin/python3


def weight_average(my_list=[]):
    sumOfProduct = 0
    sumOfValue = 0
    for key, value in dict(my_list):
        sumOfProduct += (key * value)
        sumOfValue += value
    return sumOfproduct / sumOfValue
