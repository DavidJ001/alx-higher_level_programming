#!/usr/bin/python3

"""
Base Module
Handles the creation of unique IDs
"""


class Base:
    """The base class"""
    __nb_objects = 0

    def __init(self, id=None):
        if id is None:
            self.id = Base.__nb_objects
            Base.__nb_objects += 1
        else:
            self.id = id
