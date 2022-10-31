#!/usr/bin/python3

"""Creating a Rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initializing the Rectangle class. """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This defines the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """special method to return a printable string. """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
