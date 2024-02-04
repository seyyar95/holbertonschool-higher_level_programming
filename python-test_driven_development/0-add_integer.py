#!/usr/bin/python3
"""This module contains add_integer function"""

def add_integer(a, b=98):
    """a function that adds 2 integers together and returns their sum
    Args:
        a: the first int
        b: the second int, default 98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
