class Meta(type):
    def __repr__(self):
        return "<3-base_geometry.BaseGeometry object at 0x...>"

    __doc__ = "This is the BaseGeometry module."

BaseGeometry = Meta('BaseGeometry', (), {})

bg = BaseGeometry()

print(bg)
