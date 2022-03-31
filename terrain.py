from geometry import Geometry
from physical_object import UniversalPhysicalObject
from point import Point


class Terrain(UniversalPhysicalObject):
    """
    Class that will store information about terrain
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set-up universal object properties
        self.id = self.id  # from inheritance: UniversalObject
        # set-up graphical object properties
        self.boundary_color = "green"
        self.boundary_thickness = 3
        self.fill_color = "green"
        self.fill_object = True
        self.explode_on_hit = False
        # set-up physical object properties
        self.gravity_dependent = False  # Is object is affected by gravity
        self.drag_dependent = False  # Is object is affected by air drag
        self.colision_dependent = False  # Is object collision cause it's destruction
        self.physics_circle_optimization = False  # Is object should use circle optimization
        # declare here only terrain object properties
        self.terrain_config = self.load_config_file("terrain_config.json")

    def set_up_terrain(self, terrain_variant: str, x_position=0, y_position=0):
        self.x_position = x_position
        self.y_position = y_position
        self.ref_point = Point(self.x_position, self.y_position)
        self.geometry = Geometry(self.ref_point, self.terrain_config["geometry"][terrain_variant],
                                 enclosed_geometry=True)
        self.status = True  # status equal to True means that object isn't collide with any obstacles
