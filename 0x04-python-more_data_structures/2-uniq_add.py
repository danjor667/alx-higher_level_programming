#!/usr/bin/python3


def uniq_add(my_list=[]):
    seen = set()
    count = 0
    for ele in my_list:
        if ele in seen:
            continue
        coutnt += ele
        seen.add(ele)
    return count
