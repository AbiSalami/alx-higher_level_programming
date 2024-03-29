#!/usr/bin/python3
"""
Module: 2-square
"""


class Square:
    """
    Represents a square with private instance attribute: size.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance with an optional size.

        Args:
            size (int): The size of the square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
