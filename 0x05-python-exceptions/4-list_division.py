#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            ans = my_list_1[i] / my_list_2[i]
            res.append(ans)
        except (TypeError, ZeroDivisionError, IndexError):
            ans = 0
            if TypeError:
                print("wrong type")
            elif ZeroDivisionError:
                print("division by 0")
            else:
                print("out of range")
            res.append(ans)
        finally:
            return res
