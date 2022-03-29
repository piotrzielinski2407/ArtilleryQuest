from id_handler import IdHandler


class UniversalObject:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.x_position = None
        self.y_position = None
        self.ref_point = None
        self.geometry = None
        self.status = None  # status equal to True means that object isn't collide with any obstacles
        self.id = IdHandler().set_id(self)


if __name__ == '__main__':
    object1 = UniversalObject()
    object2 = UniversalObject()
    print(object1.id, object2.id)
