"""
2-inherits_from module

Defines a function that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: Object to check.
        a_class: Class to check against.

    Returns:
        True if obj is an instance of a class that inherited from a_class, otherwise False.
    """
    return issubclass(type(obj), a_class)