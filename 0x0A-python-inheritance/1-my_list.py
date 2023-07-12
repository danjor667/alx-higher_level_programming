#!/usr/bin/python3


"""a class MyList
"""


class Mylist(list):
    """
    class that ingerits from the list class
    """
    def print_sorted(self):
        """
        method print the ele of a list in sorted orde
        """
        print(sorted(self))
