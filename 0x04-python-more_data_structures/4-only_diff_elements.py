#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    new_set = set()
    for ele in set_1:
        if ele not in set_2:
            new_set.add(ele)
    return new_set
