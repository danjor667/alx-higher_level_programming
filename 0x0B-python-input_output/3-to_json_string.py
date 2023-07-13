#!/usr/bin/python3
"""
function to_json_string
"""
import json


def to_json_string(my_obj):
    """
    gives the a json string repr of a file object
    Args:
        my_obj: the object
    Return:
        None
    """
    return json.dumps(my_obj)
