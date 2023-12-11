def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        True if obj is an instance of a class that inherited from a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class

