#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Check if `obj` is an instance of, or if it's an instance of a class that
    inherited from, the specified `a_class`.

    Args:
        obj: Object to check.
        a_class: Specified class.

    Returns:
        True if `obj` is an instance of, or inherited from, the specified `a_class`;
        otherwise, False.
    """
    return isinstance(obj, a_class)