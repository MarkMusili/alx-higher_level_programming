#!/usr/bin/python3
"""
This module defines a base class:
that will the the parent class of all the other class
"""
import json


class Base:
    """
    This class manages the id attribute \
    for the rest of the classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Arg:
            id (int): Number associated with an instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serilize the json representation
        Return:
            A JSON representation
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(f"{list_dictionaries}")

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save the json representation
        arg:
            list_objs : list of objects
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as f:
            f.write(json_string)

    def from_json_string(json_string):
        """
        Deserilize the json representation
        Arg:
            json_string (str): serilized data
        Return:
            deserilized data
        """
        if json_string is None:
            return "[]"
        return json.loads(f"[{json_string}]")

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a class
        Arg:
            dictionary: pointer to  a dictionary
        Return:
             A class
        """
        dummy = cls(1, 6, 1, 1)
        dummy.update(**dictionary)
        return dummy