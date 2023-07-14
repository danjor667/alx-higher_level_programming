#!/usr/bin/python3
"""
defines from_json_string
"""
import json


def from_json_string(my_str):
    """
    gives a python object from its json string repr
    Args:
        ny_str: json str repr
    Return:
        python obj
    """
    return json.loads(my_str)
