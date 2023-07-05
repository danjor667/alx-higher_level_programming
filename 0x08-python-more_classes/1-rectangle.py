#!/usr/bin/python3
'''
class that defines a rectangle
'''


class Rectangle:
    """
    intialising an instance
    """
    def __init__(self, width=0, height=0):
        """ init new instances
            Args:
                width (int) the width of the rectangle
                height (int) the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property getter
            Return:
                the value of the width
        """
        return self.__width

    @property
    def height(self):
        """ property setter
            Return:
                value o fthe height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
            Args:
                value (int): the value of ythe new height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """ width setter

            Args:
                value (int): the new valuye of width
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
