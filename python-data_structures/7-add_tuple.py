#!/usr/bin/python3
def check_tuple(tuple_n=()):
    if len(tuple_n) == 0:
        return 0, 0
    elif len(tuple_n) == 1:
        return tuple_n[0], 0
    else:
        return tuple_n


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_1 = check_tuple(tuple_a)
    tuple_2 = check_tuple(tuple_b)
    return tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1]
