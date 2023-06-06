#!/usr/bin/python3
"""
4. Text indentation
"""
def text_indentation(text):
    """
    prints a text with 2 new lines after each character ., ? and :

    Args:
        text:string to be printed

    Raises:
    TypeError: when text is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be string")
    result = ""
    chrts = [".", "?", ":"]
    for i in text:
        result += i
        if i in chrts:
            result += "\n\n"

    print(result)
