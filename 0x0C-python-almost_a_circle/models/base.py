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

    def to_json_string(list_dictionaries):
        """
        Return:
            A JSON representation
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(f"{list_dictionaries}")
