def __init__(self, size=0):
    """Initialize the Square instance"""
    try:
        size = int(size)
    except ValueError:
        raise ValueError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    self.__size = size