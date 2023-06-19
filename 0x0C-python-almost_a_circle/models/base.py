#!/usr/bin/python3

"""
1. Base class
"""
import json


class Base:
    """
    base class for other classes in the project
    This class has a private class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        Args:
           id: to be asigned to the private attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a json string of list_dictionaris

        Args:
            list_dictionaries; to be converted into json string
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class method that writes a json string rep of list_objs into a file

        Args:
            cls: class instance
            list_objects: list of instances that inherit from base
        """
        if list_objs is None:
            list_objs = []

        c_name = cls.__name__
        f_name = f"{c_name}.json"
        j_string = cls.to_json_string([obj.to_dictionary() for i in list_objs])

        with open(f_name, 'w') as file:
            file.write(j_string)

    @staticmethod
    def from_json_string(json_string):
        """
        method that returns a python string

        Args:
            json_string: string to be converted back to python
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        class method that returns an instance with all attributes

        Args:
            cls: class
            dictionary: double pointer to dictionary
        """
        tmp = cls(width=0, height=0)
        tmp.update(**dictionary)
        return tmp

    @classmethod
    def load_from_file(cls):
        """
        class method that returns a list of instances

        Args:
            cls: child class

        Returns:
            list of instances from the file
        """
        c_name = cls.__name__
        f_name = f"{c_name}.json"

        try:
            with open(f_name, 'r') as file:
                j_data = file.read()
        except FileNotFoundError:
            return []

        p_data = cls.from_json_string(j_data)
        temp = []

        for item in p_data:
            instance = cls.create(**item)
            temp.append(instance)
        return temp
