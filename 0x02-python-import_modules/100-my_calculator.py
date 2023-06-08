#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, mul, div, sub


def operation(*args):
    if len(args) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if args[1] == "+":
            print("{} + {} = {}".format(arg[0], arg[2], add(arg[0], arg[2])))
            exit(0)
        elif args[1] == "-":
            print("{} - {} = {}".format(arg[0], arg[2], sub(arg[0], arg[2])))
            exit(0)
        elif args[1] == "*":
            print("{} * {} = {}".format(arg[0], arg[2], mul(arg[0], arg[2])))
            exit(0)
        elif args[1] == "/":
            print("{} / {} = {:d}".format(arg[0], arg[2], div(arg[0], arg[2])))
            exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    operation(*argv[1:])
