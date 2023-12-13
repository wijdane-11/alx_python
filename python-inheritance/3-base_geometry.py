class Meta(type):
    def __repr__(self):
        return "<3-base_geometry.BaseGeometry object at 0x...>"

class BaseGeometry(metaclass=Meta):
    pass

bg = BaseGeometry()

print(dir(bg))
print(dir(BaseGeometry))