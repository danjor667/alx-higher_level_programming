#!/usr/bin/python3
"""
defining a class Square
"""
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__():
        return f"[{Square}] ({self.id}) {self.__x}/{self.y} - {self.__width}"
    
    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, size):
        self.__width = size
        self.__height = size

    def update(self, *args, **kwargs):
        arg = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i in range(len(args)):
                setattr(self, arg[i], args[i])
        elif kwargs:
            for attr in kwargs:
                setattr(self, attr, kwargs[attr])
        else:
            raise ValueError("update: positional and/or keyword arg required")

    def to_dictionary(self):
        a = self.__dict__
        my_dict = {key[9:]: value for key, value in a}
        return my_dict
