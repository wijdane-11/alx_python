# models/square.py
from models.rectangle import Rectangle

class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): X coordinate of the square. Defaults to 0.
            y (int, optional): Y coordinate of the square. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overrides the __str__ method to provide a custom string representation."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        self.width = value
        self.height = value
