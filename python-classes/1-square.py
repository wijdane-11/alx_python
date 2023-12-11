#!/usr/bin/python3
"""Defines a Square class."""

class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

# Test cases
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)