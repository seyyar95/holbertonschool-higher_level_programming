#!/usr/bin/python3
"""module doc"""


def append_write(filename="", text=""):
    """function doc"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
