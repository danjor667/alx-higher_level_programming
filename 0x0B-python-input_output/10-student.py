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
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        returns a dict repr of
        an instance
        """
        my_dict = self.__dict__
        if attrs is None:
            return my_dict
        elif isinstance(attrs, list):
            new_dict = {}
            for key, value in my_dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
