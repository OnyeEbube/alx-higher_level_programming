#!/usr/bin/python3

""" Creating a function. """
import json


def load_from_json_file(filename):
    """ This function creates an object from a JSON file."""
    with open(filename, 'r', encoding="utf-8") as x:
        return json.load(x)
