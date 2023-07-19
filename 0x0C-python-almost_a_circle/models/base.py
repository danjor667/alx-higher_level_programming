#!/usr/bin/python3
"""
defining a class Base
"""


class Base():
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialising instance
        """
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
