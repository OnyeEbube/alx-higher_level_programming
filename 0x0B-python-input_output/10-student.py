#!/usr/bin/python3

""" Creating a class """


class Student:
    """ A class that defines a student by first_name, last_name, and age. """
    def __init__(self, first_name, last_name, age):
        """ Initializing an instance of the clas. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ A method that retrievews a dictionary representation of a Student
        instance."""
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return obj
            d_list = {}
            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] == obj[satr]
            return d_list
        return obj
