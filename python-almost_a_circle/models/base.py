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
        """ Dictionary to JSON string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of
        the JSON string representation"""
        return json.loads(json_string)
