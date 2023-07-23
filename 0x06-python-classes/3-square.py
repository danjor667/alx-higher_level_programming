#!/usr/bin/python3
"""
defineing a class Square
"""


class Square():
    """
    class Square
    """
    def __init__(self, size=0):
        """
        initializing an instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        calculate the area of the square
        """
        return self.__size * self.__size
