#!/usr/bin/python3
from add_0 import add
if __name__ == "main":
    a = 1
    b = 2
    print("{a:d} + {a:d} = {:d}".format(a, b, add(a, b)))
