class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initializes a Square instance with a size.

        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than or equal to 0.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
