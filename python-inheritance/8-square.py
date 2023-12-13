class BaseGeometry:
    """A class for basic geometric operations.

    Attributes:
        name (str): The name of the value.
        value (int): The value to validate.

    Methods:
        area(): Raises an exception since the area calculation is not implemented.
        integer_validator(name, value): Validates if the value is an integer and greater than 0.
    """

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
