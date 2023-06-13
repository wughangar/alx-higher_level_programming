#!/usr/bin/python3

"""
13. Search and update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that searches and appends certain string

    Args:
        filename: name of the file to be searched
        search_string: variable to string to be searched
        new_string: string to be appended
    """
    with open(filename, "r+") as f:
        lines = f.readlines()

        for l in lines:
            f.write(l)
            if search_string in l:
                f.write(new_string)
