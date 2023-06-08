#!/usr/bin/python3
from sys import argv
from calculator_1 import add, mul, div, sub


def operation(*args):
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1
    else:
        if args[1] == "+":
            print("{} + {} = {}".format(arg[0], arg[2], add(arg[0], arg[2])))
            return
        elif args[1] == "-":
            print("{} - {} = {}".format(arg[0], arg[2], sub(arg[0], arg[2])))
            return
        elif args[1] == "*":
            print("{} * {} = {}".format(arg[0], arg[2], mul(arg[0], arg[2])))
            return
        elif args[1] == "/":
            print("{} / {} = {}".format(arg[0], arg[2], div(arg[0], arg[2])))
            return
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            return 1


if __name__ == "__main__":
    operation(*argv[1:])
