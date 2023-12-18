class Base:
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # assign id if provided
        else:
            type(self).__nb_objects += 1  # increment __nb_objects for each new instance
            self.id = type(self).__nb_objects  # assign incremented value as id

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)  # Output: 1

    b2 = Base()
    print(b2.id)  # Output: 2

    b3 = Base()
    print(b3.id)  # Output: 3

    b4 = Base(12)
    print(b4.id)  # Output: 12

    b5 = Base()
    print(b5.id)  # Output: 4
