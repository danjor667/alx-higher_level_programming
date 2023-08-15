#!/usr/bin/python3
"""
doc
"""


def test_int(x):
    return all(isinstance(ele, int) for ele in x)


def test_float(x):
    return all(isinstance(ele, float) for ele in x)


def test_row(mtrx):
    n = len(mtrx[0])
    for row in mtrx:
        if len(row) != n:
            return False
    return True


def matrix_divided(matrix, div):
    """
    doc
    """
    new_matrix = [[] for i in range(len(matrix))]

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) \
            or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be \
a matrix (list of lists) of integers/floats")
    if not test_row(matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(test_int(x) for x in matrix) \
            and not all(test_float(x) for x in matrix):
        raise TypeError("matrix must be \
a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / div, 2))
    return new_matrix
