#!/usr/bin/python3
"""
3. Print square
"""
def print_square(size):
    """
    function that prints square

    Args:
        size: size of the square in terms of length

    Raises:
        TypeError: when size is not an int
        ValueError: when size if less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
