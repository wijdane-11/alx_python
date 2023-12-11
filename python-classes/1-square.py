def __init__(self, size=0):
    """Initialize the Square instance"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    self.__size = size