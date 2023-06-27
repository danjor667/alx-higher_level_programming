#!/usr/bin/python3
'''Class called Square which represents a square''' 
  
  
class Square:
         '''Square class with private size attr'''
         def __init__(self, size):
             '''Initializes instances of Square.
             Args:size (int): Represents the size of one side of the square. 
         '''
         self.__size = size
