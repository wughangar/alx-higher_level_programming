#!/usr/bin/python3

"""
2. Append to a file
"""


def append_write(filename="", text=""):
    """
    function that appends text to file and returns number of charcters added

    Args:
       filename: name of the file to have text appended to
       text: text to be appended

    Return: number of characters appended

    """
    with open(filename, "a", encoding="UTF8") as f:
        f.write(text)
        return len(text)
