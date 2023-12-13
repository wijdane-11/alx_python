#!/usr/bin/python3
"""
Module 8-square

This module contains the Square class inheriting from Rectangle.
"""
class BaseGeometry:
    """A class defining geometric operations."""

    def area(self):
        """Raises an Exception to indicate that the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the 'value' is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class representing a Rectangle."""

    def __init__(self, width, height):
        """Initializes the Rectangle instance with given width and height."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Computes the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string describing the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """A class representing a Square."""

    def __init__(self, size):
        """Initializes the Square instance with given size."""
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string describing the square."""
        return f"[Rectangle] {self.__size}/{self.__size}"


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
