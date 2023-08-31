#!/usr/bin/python3

"""
9. Student to JSON
"""


class Student:
    """
    class that defines a strudent
    """
    def __init__(self, first_name, last_name, age):
        """
        student method with instantiation of several variables

        Args:
            first_name: first name of the student
            last_name: last name of the student
            ge: age of the student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        public method that retrives a dict rep

        Returns: a dict representing the instance student
        """
        jdict = {}
        for a, value in self.__dict__.items():
            if a.startswith("__"):
                continue
            jdict[a] = value
        return jdict
