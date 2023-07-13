#!/usr/bin/python3
"""
function append_wirte
"""


def append_write(filename="", text=""):
    """
    appending text to a file
    Args:
        filename: name;of the;file
        text: string to append
    Return:
        num of char appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        num = f.write(text)
        return num
