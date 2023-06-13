#!/usr/bin/python3

"""
10. Student to JSON with filter
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

    def to_json(self, attrs=None):
        """
        public method that retrives a dict rep

        Returns: a dict representing the instance student
        """
        if attrs is None:
            return self.__dict__
        jdict = {}
        for a in attrs:
            if isinstance(a, str) and hasattr(self, a):
                jdict[a] = getattr(self, a)
        return jdict
