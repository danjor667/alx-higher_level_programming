#!/usr/bin/python3
"""a class, List"""


class Mylist(list):
    """
    class that ingerits from the list class
    """
    def print_sorted(self):
        """
        method that prints the ele of a list in sorted order
        """
        print(sorted(self)
