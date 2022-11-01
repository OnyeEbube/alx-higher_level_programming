#!/usr/bin/python3

""" Creating a class """


class Student:
    """ A class that defines a student by first_name, last_name, and age. """
    def __init__(self, first_name, last_name, age):
        """ Initializing an instance of the clas. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A method that retrievews a dictionary representation of a Student
        instance."""
        return self.__dict__.copy()
