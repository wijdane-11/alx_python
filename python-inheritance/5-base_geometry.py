"""Module containing the BaseGeometry class.

This module provides the BaseGeometry class, which includes methods for basic geometry operations.

Classes:
    BaseGeometry: A class representing basic geometric operations.

"""

class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
