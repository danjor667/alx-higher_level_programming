#!/usr/bin/python3
"""
defines function load_from_json_file
"""

import json


def load_from_json_file(filename):
    """
    creats an obj fron a json file
    Args:
        filename: file to;read from
    Return:
        python obj
    """
    with open(filename) as f:
        obj = json.load(f)
        return obj
