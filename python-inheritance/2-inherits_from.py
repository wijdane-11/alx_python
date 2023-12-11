a = 1
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
else:
    print("{} does not inherit from class {}".format(a, int.__name__))
