#!/usr/bin/python3

"""
1. Write to a file
"""


def write_file(filename="", text=""):
    """
    function that writes into files and creates then if not created

    Args:
        filename: name of the file
        text: content to be written

    Returns:
        number of characters writte
    """
    with open(filename, "w", encoding="UTF8")as f:
        num = f.write(text)
    return num
