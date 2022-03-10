from geometry import Geometry
from universal_object import UniversalObject
from point import Point


class Terrain(UniversalObject):
    """
    Class that will store information about terrain
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # declare here only terrain object properties
        self.terrain_config = self.load_config_file("terrain_config.json")
        # set-up universal object properties
        self.gravity_dependent = False  # Is object is affected by gravity
        self.drag_dependent = False  # Is object is affected by air drag
        self.colision_dependent = False  # Is object collision cause it's destruction
        self.physics_circle_optimization = False  # Is object should use circle optimization,

    def set_up_terrain(self, terrain_variant: str, x_position=0, y_position=0):
        self.x_position = x_position
        self.y_position = y_position
        self.ref_point = Point(self.x_position, self.y_position)
        self.geometry = Geometry(self.ref_point, self.terrain_config["geometry"][terrain_variant],
                                 enclosed_geometry=False)
        self.status = True  # status equal to True means that object isn't collide with any obstacles

    def simulate_time_step(self, time_scale=None, gravity=None,
                           wind_speed=None, density=None):
        self.geometry.update(self.ref_point)
