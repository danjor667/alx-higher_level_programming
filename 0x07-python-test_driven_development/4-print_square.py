#!/usr/bin/python3
"""
doc
"""


def print_square(size):
    """
    doc
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    s = "#" * size
    for i in range(size):
        print(s)
