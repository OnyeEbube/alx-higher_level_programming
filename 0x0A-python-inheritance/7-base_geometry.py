#!/usr/bin/python3

""" Creating a class. """


class BaseGeometry:
    """ This is a class that defines an area method and integer_validator
    method
    """
    def area(self):
        """ An empty function. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
