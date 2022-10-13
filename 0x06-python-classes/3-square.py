#!/usr/bin/python3

"""Defining a class Square."""


class Square:
    """Class Square that defines the size and area of a square."""

    def __init__(self, size=0):
        """Method to initialize the size of the square object."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
    def area(self):
        """Initializing a method are to return the area of the square."""

        return self.__size
