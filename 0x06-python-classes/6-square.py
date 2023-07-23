#!/usr/bin/python3
"""
defineing a class Square

"""


class Square():
    """
    class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializing an instance
        """
        self.position = position
        self.size = size

    def area(self):
        """
        calculate the area of the square
        """
        return self.__size * self.__size

    @property
    def position(self):
        """
        property getter
        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        property setter
        """
        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) != int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) != int or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

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
        x = " " * self.__position[0]
        sym = x + "#" * self.__size
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            print(sym)
