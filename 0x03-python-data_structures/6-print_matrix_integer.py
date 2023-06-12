#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print ("{row}, {col}".format(row, col))
