#!/usr/bin/python3
"""
a class Rectangle thet inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """
    def __init__(self, width, height):
        """
        initialising...
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
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
