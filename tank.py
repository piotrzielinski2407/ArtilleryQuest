from geometry import Geometry
from point import Point
from physical_object import UniversalPhysicalObject


class Tank(UniversalPhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set-up universal object properties
        self.id = self.id  # from inheritance: UniversalObject
        self.x_position = self.x_position  # from inheritance: UniversalObject
        self.y_position = self.y_position  # from inheritance: UniversalObject
        self.ref_point = self.ref_point  # from inheritance: UniversalObject
        self.geometry = self.geometry  # from inheritance: UniversalObject
        # set-up graphical object properties
        self.boundary_color = 'black'  # boundary color for graphic render
        self.boundary_thickness = 3  # thickness of boundary line
        self.fill_color = 'black'  # color to fill in
        self.fill_object = True  # if True, graphic render will fill created boundary with fill_color
        self.explode_on_hit = False
        # set-up physical object properties
        self.gravity_dependent = False  # Is object is affected by gravity
        self.drag_dependent = False  # Is object is affected by air drag
        self.colision_dependent = False  # Is object collision cause it's destruction
        self.check_for_collision = False  # If collision should be checked on that item
        self.physics_circle_optimization = False  # Is object should use circle optimization,
        # not recommended for big objects
        # declare here only tank object properties
        self.tank_config = self.load_config_file("tank_config.json")

    def set_up_tank(self, x_position=10, y_position=20):
        self.x_position = x_position
        self.y_position = y_position
        self.ref_point = Point(self.x_position, self.y_position)
        self.geometry = Geometry(self.ref_point, self.tank_config["geometry"],
                                 enclosed_geometry=True)
        self.status = True  # status equal to True means that object isn't collide with any obstacles
