#!/usr/bin/python3

"""Creating a clas Square."""


class Square:

    """Creating a method as an object of class."""

    def __init__(self, size=0):
        """Initializing a method for square."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size mut be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """Defining a method for area of square."""
        return (self.__size ** 2)

    def my_print(self):
        """Defining a method to print square."""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end='')
            print()

    @property
    def size(self):
        """Method that returns the size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """Method to set the value of size."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
