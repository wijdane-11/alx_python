class BaseGeometry:
    """A class representing basic geometry operations.

    Methods:
        area(self): Raises an Exception with the message 'area() is not implemented'.
        integer_validator(self, name, value): Validates the value as an integer.

    """

    def area(self):
        """Raises an Exception for unimplemented area calculation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the given value as an integer.

        Args:
            name (str): Name of the value being validated.
            value (int): Value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
