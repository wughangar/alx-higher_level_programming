#!/usr/bin/python3
"""
1.my list
"""


class MyList(list):
    """
    a child class from list
    """
    def print_sorted(self):
        """
        prints a sorted list of ints
        """
        new_list = sorted(self)
        print(new_list)
