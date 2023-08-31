#!/usr/bin/python3

"""
0. Read file
"""


def read_file(filename=""):
    """
    function that reads files and prints in stdout

    Args:
        filename="" : file name
    """
    with open(filename, "r", encoding="UTF8") as f:
        content = f.read()
        print(content)
