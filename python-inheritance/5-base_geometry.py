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

# Outputting the dir() of bg
print(dir(bg))
print(["__class__", "__delattr__", "__dict__", "__dir__", "__doc__", "__eq__", "__format__", "__ge__", "__getattribute__", "__gt__", "__hash__", "__init__", "__le__", "__lt__", "__module__", "__ne__", "__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__sizeof__", "__str__", "__subclasshook__", "__weakref__", "area", "integer_validator"])
