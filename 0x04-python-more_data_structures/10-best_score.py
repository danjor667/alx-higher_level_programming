#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        maximum = 0
        name = ""
        for key, value in a_dictionary.items():
            if value > maximum:
                maximum = value
                name = key
        return name
    else:
        return None
