#!/usr/bin/python3
"""
Module: 1-square
"""


class Square:
    """
    Defines a sqaure with private instance attribute: size.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance with an optional size.
        

        Args:
           size (int): The size of the new square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
