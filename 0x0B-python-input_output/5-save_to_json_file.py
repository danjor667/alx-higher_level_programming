#!/usr/bin/python3
"""
defines;funct save_to_json_file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    write a json str repr of an obj in a file
    Args:
        my_obj: obj to be save
        filename: file to be saved in
    Return:
        None
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
