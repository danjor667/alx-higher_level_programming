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

    def __str__(self):
        """ string representation of a trianglr
            Return:
                a tiangle drawn with #
        """
        ans = ""
        s = "#" * self.width + "\n"
        if self.width == 0 or self.height == 0:
            return ans
        for i in range(self.height):
            if i == self.height - 1:
                ans += "#" * self.width
            else:
                ans += s
        return ans

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

    def area(self):
        """ getting area
            Return:
                area
        """
        return self.width * self.height

    def perimeter(self):
        """ calculating the perimeter
            Return:
                perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)
