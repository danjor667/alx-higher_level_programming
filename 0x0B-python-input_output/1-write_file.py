#!/usr/bin/python3
"""
function write_file
"""


def write_file(filename="", text=""):
    """
    writing into a file
    Args:
    text: string to weite
    filename: name of file
    Return:
        num of char written
    """
    with open(filename, "w", encoding="utf-8") as f:
        num = f.write(text)
        return num
