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
        self.__size = size

    def area(self):
        """
        calculate the area of the square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        attribute getter
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        attribute setter
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be > 0")
        self.__size = size

    def my_print(self):
        """
        print a sqaure to stdout using "#"
        """
        sym = "#" * self.__size
        if self.__size == 0:
            print("")
            return
        for i in range(self.__size):
            print(sym)
