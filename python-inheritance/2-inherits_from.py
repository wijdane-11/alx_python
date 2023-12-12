#!/usr/bin/python3
"""
This script demonstrates the usage of the 'inherits_from' function to check if an object is
an instance of a class that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited from a specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if obj is an instance of a class that inherited from a_class; otherwise, False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class

# Example usage:
a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))