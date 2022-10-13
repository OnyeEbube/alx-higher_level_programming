#!/usr/bin/python3

"""Creating a class Square."""


class Square:
    """Defining a class Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing methods with private attributes."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
        if (len(position) == 2):
            for i in range(2):
                if position[i] < 0:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
                else:
                    self.__position = position

    def area(self):
        """Creating a method for square"""
        return (self.__size ** 2)

    def my_print(self):
        """Creating a method for square."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print("#", end='')
                print()


    @property
    def size(self):
        """Retrieving the size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the value of size value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieving position values."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setting the value of the position value."""
        if (len(position) == 2):
            for i in range(2):
                if position[i] < 0:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
                else:
                    self.__position = value
