#!/usr/bin/python3
"""module doc"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”
    """
    with open(filename, "r") as file:
        return json.load(file)
