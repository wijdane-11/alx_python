class BaseGeometry:
    """A class for basic geometric operations.

    This class contains methods for basic geometric operations such as calculating area
    and validating integer values.

    Methods:
        area(self): Raises an Exception indicating 'area() is not implemented'.
        integer_validator(self, name, value): Validates the given value as an integer.

    """

    def area(self):
        """Raise an Exception for unimplemented area calculation."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the given value as an integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# Creating an instance of BaseGeometry
bg = BaseGeometry()
out
# Outputting the dir() of bg
print(dir(bg))
