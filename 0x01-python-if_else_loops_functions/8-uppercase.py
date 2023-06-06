#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        if 97 <= ord(char) <= 123:
            new_str += chr(ord(char) - 32)
        else:
            new_str += chr(ord(char))
    print("{}".format(new_str))
