#!/usr/bin/python3
"""Module doc"""


def read_file(filename=""):
    """function doc"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
