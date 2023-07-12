#!/usr/bin/python3
"""
class MyInt
"""


class MyInt(int):
    """
    class MyInt
    """
    def __init__(self):
        super().__init__(self)

    def __eq__(self, other):
        """
        equality magic method inverted
        """
        return (float(self) != float(other))

    def __ne__(self, other):
        """
        non equality magics method inversted
        """

        return float(self) == float(other)
