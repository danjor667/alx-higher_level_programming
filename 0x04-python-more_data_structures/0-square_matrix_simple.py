#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    n = len(matrix)
    new_matrix = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[i][j] ** 2
    return new_matrix
