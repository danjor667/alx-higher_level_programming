#!/usr/bin/python3


def common_elements(set_1, set_2):
    new_set = set()
    for ele in set_1:
        if ele in set_2:
            new_set.add(ele)
    return new_set


"""
can also use:
    return set_1 & set_2
    """
