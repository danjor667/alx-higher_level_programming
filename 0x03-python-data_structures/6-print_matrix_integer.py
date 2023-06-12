#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in range(len(row)):
            if col > len(row) - 1:
                print ("{col:d}, end=''".format(row[col]))
            else:
                print("{col:d}".format(row[col]))
