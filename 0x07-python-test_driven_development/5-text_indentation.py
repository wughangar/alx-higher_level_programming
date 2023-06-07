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
    rsl = ""

    for i in text:
        if i == '.' or i == '?' or i ==  ':':
            rsl += i + "\n\n"
        else:
            rsl += i
    print(rsl)
