#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """A class representing a Rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return the representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    r = Rectangle(3, 5)
