#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes the square"""
        self.__size = size
        self.__check_size(size)

    def __check_size(self, size):
        """Checks if the size is an integer and >= 0"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        self.__size = value
        self.__check_size(value)

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)
