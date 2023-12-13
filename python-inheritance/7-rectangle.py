class BaseGeometry:
    """
    A class defining geometric operations.

    Methods:
    - area(): Raises an Exception with the message 'area() is not implemented'.
    - integer_validator(name, value): Validates that 'value' is an integer and greater than 0.

    Raises:
    - TypeError: If 'value' is not an integer.
    - ValueError: If 'value' is less than or equal to 0.
    """

    def area(self):
        """Raises an Exception to indicate that the area method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the 'value' is a positive integer.

        Args:
        - name: A string representing the name of the value.
        - value: An integer value to be validated.

        Raises:
        - TypeError: If 'value' is not an integer.
        - ValueError: If 'value' is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a Rectangle.

    Attributes:
    - __width: Width of the rectangle.
    - __height: Height of the rectangle.

    Methods:
    - __init__(width, height): Initializes the Rectangle instance.
    - area(): Computes the area of the rectangle.
    - __str__(): Returns a string describing the rectangle in the format '[Rectangle] <width>/<height>'.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance with given width and height.

        Args:
        - width: Width of the rectangle.
        - height: Height of the rectangle.
        """
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
