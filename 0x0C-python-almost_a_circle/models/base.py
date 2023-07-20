#!/usr/bin/python3
"""
defining a class Base
"""
import json


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
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__
        my_list = []
        if list_objs is None or list_objs == []:
            my_list = []
        else:    
            for ele in list_objs:
                my_list.append(ele.to_dictionary())
        data = cls.to_json_string(my_list)
        with open(f"{file_name}.json", "w") as f:
            f.write(data)

    @statictmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        name = cls.__name__
        if name == "Rectangle":
            rectangle = cls(5,10)
            rectangle.update(**dictionary)
            return rectangle
        else:
            square = cls(2)
            square.update(**dictionary)
            return square

