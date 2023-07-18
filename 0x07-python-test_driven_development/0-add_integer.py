#!/usr/bin/python3
"""
function that return the int
sum of 2 numbers
"""


def add_integer(a, b=98):
    """
    adds two values, int or float
    return an int
    Args:
        a, b: int or float
    Returns:
        int
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

