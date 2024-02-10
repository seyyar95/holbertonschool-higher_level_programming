#!/usr/bin/python3
"""Module Doc"""


def write_file(filename="", text=""):
    """function doc"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
