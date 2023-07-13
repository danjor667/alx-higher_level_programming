#!/usr/bin/python3
"""
defines function pascal_triangle
"""


def pascal_triangle(n):
    """
    generates list of num representing
    pascal triagle
    Args:
         n: degree of triagel
    Returns:
        list
    """
    result = [[1]]
    if n <= 0:
        return []
    if n == 1:
        return result
    def getnext(prev):
        new_row = [1]
        a = len(prev)
        i = 0
        while i <= a - 2:
            ele = prev[i] + prev[i + 1]
            new_row.append(ele)
            i += 1
        new_row.append(1)
        return new_row
    m = 0
    while m <= n - 2:
        result.append(getnext(result[m]))
        m += 1
    return result
