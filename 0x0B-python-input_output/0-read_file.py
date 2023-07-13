#!/usr/bin/python3
"""
defines the read_file funct
"""


def read_file(filename=""):
    """
    reads a file
    Args:
        filename
    Return:
        None
    """
    with open(filename) as f:
        file = f.read()
        print(file)
