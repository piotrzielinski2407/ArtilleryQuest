from graphic_object import UniversalGraphicObject


class UniversalPhysicalObject(UniversalGraphicObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gravity_dependent = None  # Is object is affected by gravity
        self.drag_dependent = None  # Is object is affected by air drag
        self.colision_dependent = None  # Is object collision cause it's destruction
        self.physics_circle_optimization = None  # Is object should use circle optimization,

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_value):
        if isinstance(new_value, bool):
            if self.colision_dependent:
                self._status = new_value
            else:
                self._status = True

    @staticmethod
    def load_config_file(file_name):
        """
        Function that will load json file base on provided filename
        :param file_name:
        :return:file
        """
        import json
        with open(file_name, "r") as json_file:
            file = json.load(json_file)
        return file

    def simulate_time_step(self, time_scale=None, gravity=None,
                           wind_speed=None, density=None):
        pass

    def collision_occur(self):
        """
        Method that will be called if collision on certain object have place
        :return:
        """
        if self.colision_dependent is True:
            self.status = False
