#!/usr/bin/python3
from sys import argv


def add(*args):
    result = 0
    if len(args) == 0:
        print("{:d}".format(result))
    else:
        for i in range(len(args)):
            result += int(args[i])
        print("{}".format(result))


if __name__ == "__main__":
    add(*argv[1:])
