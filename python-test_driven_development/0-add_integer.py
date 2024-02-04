#!/usr/bin/python3
def add_integer(a, b=98):
    """ A function that adds 2 integers together and returns their sum

    >>> add_integer(2, 3)
    5
    >>> add_integer(1, -1)
    0
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
