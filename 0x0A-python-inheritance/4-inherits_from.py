#!/bin/bash/python3
"""
funct,
"""


def inherits_from(obj, a_class):
    """
    a funt to verify is an obj is an instance of subclass of class
    Args:
        obj
        a_class
    Return:
        bool
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
