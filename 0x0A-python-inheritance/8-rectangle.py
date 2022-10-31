#!/usr/bin/python3

"""Creating a class that inherits from class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ This is a class that inherits from the BaseGeometry class."""
    def __init__(self, width, height):
        """initializes instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
