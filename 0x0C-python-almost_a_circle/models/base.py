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
        Class constructor
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
        return json.dumps(list_dictionaries)

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
        if json_string is None or json_string is []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a class instance
        Arg:
            dictionary: pointer to  a dictionary
        Return:
             A class
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 6)
        else:
            dummy = cls(4)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Read from a json file
        Return:
            list of instances
        """
        filename = cls.__name__ + ".json"
        list_of_instances = []
        try:
            with open(filename, 'r') as f:
                file_contents = f.read()
                contents = cls.from_json_string(file_contents)
            for item in contents:
                instance = cls.create(**item)
                list_of_instances.append(instance)
        except FileNotFoundError:
            pass
        return list_of_instances
