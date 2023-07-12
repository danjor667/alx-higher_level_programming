#!/usr/bin/python3
Rectangle = __import__('9-rectangle.py').Rectangle

"""
class Square
"""


class Square(Rectangle):
    """
    class Square
    """
    def __init__(self, size):
        """
        inisilising an obj
        """
        super().integer_validator(size, size)
        self.__size = size

    def area(self):
        """
        calculating the size
        """
        return self.__size ** 2
