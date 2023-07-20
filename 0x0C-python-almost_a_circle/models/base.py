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
        Args
            id: id of the instance created
        """
        if id is not None:
            self.id = id
        else:
           self.__class__.__nb_objects += 1
           self.id = self.__class__.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert a list of dicts to a json string obj
        Args:
            list_dictionaries: list of dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save a json str repr of a list obj into a file
        Args:
            cls: class of obj
            list_objs: list of obj
        """
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

    @staticmethod
    def from_json_string(json_string):
        """
        retrives an obj from its json str repr
        Args:
            json_string: json_string repr of the obj
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        create an instance of a class(obj) from its dict repr
        Args:
            cls: the instance class
            dictionary: dict repr of instance
        """
        name = cls.__name__
        if name == "Rectangle":
            rectangle = cls(5,10)
            rectangle.update(**dictionary)
            return rectangle
        else:
            square = cls(2)
            square.update(**dictionary)
            return square

