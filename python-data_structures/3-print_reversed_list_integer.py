#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    newlist = my_list[::-1]
    for i in newlist:
        print("{:d}".format(i))
