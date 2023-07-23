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
        self.size = size

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

    def __lt__(self, other):
        """
        comparing instances base on area "less than <'
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        comparing instances base on;area 'less than or equals to' <=
        """
        return self.area() <= other.area()

    def __eq__(self, rest):
        """
        comparing instances base on area? 'equals to' ==
        """
        return self.area() == rest.area()

    def __ne__(self, other):
        """
        compare instances base on area
        !=
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        compare base on area >
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        compare base on area >=
        """
        return self.area() >= other.area()
