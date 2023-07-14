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
<<<<<<< HEAD
=======
        super().__init__(size, size)
>>>>>>> cc23c8835e3065a088ca8d8bb80b4cef87c42897
        self.__size = size

    def area(self):
        """
        calculating the size
        """
        return self.__size ** 2
