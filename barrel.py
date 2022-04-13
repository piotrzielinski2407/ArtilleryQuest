from geometry import Geometry
from point import Point
from physical_object import UniversalPhysicalObject
from math import sin, cos, radians


class Barrel(UniversalPhysicalObject):
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
        self.boundary_thickness = 1  # thickness of boundary line
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
        self.barrel_config = self.load_config_file("barrel_config.json")
        self.barrel_angle = None
        self.geometry_points_no_angle = self.barrel_config["geometry"]
        self.geometry_points_with_angle = None
        self.barrel_is_set = False
        self.barrel_end = None

    @property
    def barrel_angle(self):
        return self._barrel_angle

    @barrel_angle.setter
    def barrel_angle(self, new_value):
        self._barrel_angle = new_value
        if new_value is not None and self.barrel_is_set is True:
            self.geometry_points_with_angle = self.apply_angle(new_value)
            self.geometry = Geometry(self.ref_point, self.geometry_points_with_angle,
                                     enclosed_geometry=True)

    def set_up_barrel(self, angle=45, x_position=10, y_position=20):
        self.x_position = x_position
        self.y_position = y_position
        self.barrel_angle = angle
        self.ref_point = Point(self.x_position, self.y_position)
        self.geometry_points_with_angle = self.apply_angle(self.barrel_angle)
        self.geometry = Geometry(self.ref_point, self.geometry_points_with_angle,
                                 enclosed_geometry=True)
        self.status = True  # status equal to True means that object isn't collide with any obstacles
        self.barrel_is_set = True

    def increase_angle(self):
        self.barrel_angle += 0.5

    def decrease_angle(self):
        self.barrel_angle -= 0.5

    def apply_angle(self, angle):
        points_to_return = []
        for point in self.geometry_points_no_angle:
            x = point[0]
            y = point[1]
            total_distance = (x ** 2 + y ** 2) ** (1/2)

            cos_v = cos(radians(angle))
            sin_v = sin(radians(angle))
            new_x_cord = round(total_distance * sin_v, 2)
            new_y_cord = round(total_distance * cos_v, 2)
            points_to_return.append([new_x_cord, new_y_cord])

        self.barrel_end = Point(points_to_return[1][0], points_to_return[1][1])
        return points_to_return
