#!/usr/bin/python3

""" Creating a class. """


class BaseGeometry:
    """This is a class that defines a method area."""
    def area(self):
        raise Exception("area() is not implemented")
