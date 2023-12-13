class Meta(type):
    def __dir__(self):
        return [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
            '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
            '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
            '__subclasshook__', '__weakref__', 'dummy_method'
        ]

    def dummy_method(self):
        pass

    __doc__ = "This is the BaseGeometry module."

BaseGeometry = Meta('BaseGeometry', (), {})

bg = BaseGeometry()

print(dir(bg))