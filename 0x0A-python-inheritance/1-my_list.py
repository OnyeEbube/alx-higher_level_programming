#!/usr/bin/python3

"""creating a class."""


class MyList(list):
    """This is a class that inherits from list."""

    def print_sorted(self):
        """Method that prints sortrd list."""
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
