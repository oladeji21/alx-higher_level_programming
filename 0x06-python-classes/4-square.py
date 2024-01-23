#!/usr/bin/python3
""" Module of Class Square"""


class Square:
    """Blueprint of a square objct"""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square."""
        return (self.__size)
