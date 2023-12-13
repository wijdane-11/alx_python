"""Module for geometric shapes."""

class BaseGeometry:
    """A class for basic geometry operations."""

    def area(self):
        """Raise an exception since the area calculation is not implemented."""
        raise NotImplementedError("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if the value is an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
