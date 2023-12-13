BaseGeometry = type('BaseGeometry', (), {'dummy_method': lambda self: None})

bg = BaseGeometry()

print(bg)
print(dir(bg))
print(dir(BaseGeometry))