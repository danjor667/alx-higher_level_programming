#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
class Rectangle that inherits from BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """
    def __init__(self, width, height):
        """
        initialising...
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        '''
        return the area of rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        '''
        string representation
        '''
        return(f"[Rectangle] {self.__width}/{self.__height}")
