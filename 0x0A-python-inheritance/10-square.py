#!/usr/bin/python3
"""
a class Square
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        inisilising an obj
        """
        super().integer_validator("size", size)
        super().__init__(self, size)
        self.__size = size

    def area(self):
        """
        calculating the size
        """
        return self.__size ** 2
