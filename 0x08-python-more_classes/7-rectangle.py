#!/usr/bin/python3
'''
class that defines a rectangle
'''


class Rectangle:
    """
    intialising an instance
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init new instances
            Args:
                width (int) the width of the rectangle
                height (int) the height of the rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __str__(self):
        """ string representation of a trianglr
            Return:
                a tiangle drawn with #
        """
        ans = ""
        s = str(self.print_symbol) * self.width + "\n"
        if self.width == 0 or self.height == 0:
            return ans
        for i in range(self.height):
            if i == self.height - 1:
                ans += str(self.print_symbol) * self.width
            else:
                ans += s
        return ans

    def __repr__(self):
        """representation of a triangle
            Return:
                Rectangle(width, height)
        """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """
        deleting an instanc
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

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
