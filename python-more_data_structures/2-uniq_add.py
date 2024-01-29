#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    return sum(map(lambda x: x, new_list))
