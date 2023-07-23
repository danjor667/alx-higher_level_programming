#!/usr/bin/python3
"""
defining a class Stident
"""


class Student():
    """
    class Student
    """
    def __init__(self, first_name, last_name, age):
        """
        initialising an instance
        """
        self.first_name = first_name
        self.last_name last_name
        self.age = age

    def to_json(self):
        """
        returns a dict repr of
        an instance
        """
        return self.__dict__
