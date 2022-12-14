#!/usr/bin/python3

""" Creating a class. """


class Base:
    """This class is empty."""
    __nb_objects = 0
    def __init__(self, id=None):
        """ Initializing an instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
