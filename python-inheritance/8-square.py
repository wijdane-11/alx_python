#!/usr/bin/python3
"""Module that defines a Square class"""

Rectangle = __import__('7-rectangle').Rectangle


def integer_validator(name, value):
    """Validates if the value is an integer greater than 0."""
    if type(value) is not int:
        raise TypeError(f"{name} must be an integer")
    if value <= 0:
        raise ValueError(f"{name} must be > 0")


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Compute the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Return a string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
