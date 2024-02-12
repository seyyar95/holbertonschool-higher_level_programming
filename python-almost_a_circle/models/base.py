#!/usr/bin/python3
"""Base class module"""
import json


class Base:
    """ Base class providing a unique
    identifier for its instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionary is None or listdictionary is []:
            return "[]"
        return json.dumps(list_dictionaries)
