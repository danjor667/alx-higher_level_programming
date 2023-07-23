#!/usr/bin/python3
"""
defining a funct
class_to_json
"""


def class_to_json(obj):
    """
    returns a dict repr of an
    obj
    """
    return obj.__dict__
