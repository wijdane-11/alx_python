"""This module defines the base geometry classes: BaseGeometry, Rectangle, and Square."""

class BaseGeometry:
    """A class defining basic geometric methods."""

    def area(self):
        """Method to calculate the area."""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """Method to validate the integer value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize the square with size."""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size} x {self.__size}"

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
