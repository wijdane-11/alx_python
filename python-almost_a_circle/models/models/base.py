# models/base.py

class Base:
    """
    Base class for managing unique IDs for instances.
    
    Private Class Attribute:
        __nb_objects (int): Counter for objects, initialized to 0.

    Public Methods:
        __init__(self, id=None): Constructor method for Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class with a unique ID.

        Args:
            id (int, optional): ID to assign to the instance. If not provided,
                                increments the counter and assigns the new value.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
