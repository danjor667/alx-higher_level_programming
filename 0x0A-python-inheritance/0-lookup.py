#!/usr/bin/python3
""" func that returns all attr and method of an obj"""


def lookup(obj):
    """
    funct to list all attribute and method of an obj
    Arg: object
    Return: a list
    """
    return dir(obj)
