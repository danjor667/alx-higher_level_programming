#!/usr/bin/python3
"""
function, is_same_class
"""


def is_same_class(obj, a_class):
    """
    function to verify if obj is an instance of a_class
    Arg:
        obj
    Returns:
        bool
    """
    return (type(obj) == a_class)
