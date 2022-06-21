#!/usr/bin/python3
class Square:
    """Represents a square.
    Private instance attribute: size.
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size
