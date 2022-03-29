from point import Point
from boundary import Boundary


class Geometry:
    """
    Geometry class - object that will keep geometry dependent information necessary for
    graphic render and physic calculations.
    """
    def __init__(self, ref_point, geometry_points_cords, enclosed_geometry=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # list of named tuples with co-ords on flat surface
        self.ref_point = ref_point  # reference point for geometry
        self.enclosed_geometry = enclosed_geometry  # parameters that geometry should be closed e.g. square
        self.geometry_points_cords = geometry_points_cords
        self.geometry_points = self.__create_geometry_points(self.geometry_points_cords)
        self.geometry_boundaries = self.__create_geometry_boundaries()
        self.x_drag_surface, self.y_drag_surface = self.__calculate_drag_surfaces()
        self.circle_radius = self.__calculate_circle_radius()

    @property
    def geometry_points_cords(self):
        return self._geometry_points_cords

    @geometry_points_cords.setter
    def geometry_points_cords(self, new_value):
        if isinstance(new_value, list):
            self._geometry_points_cords = new_value
            self.geometry_points = self.__create_geometry_points(new_value)
            self.geometry_boundaries = self.__create_geometry_boundaries()
            self.x_drag_surface, self.y_drag_surface = self.__calculate_drag_surfaces()
            self.circle_radius = self.__calculate_circle_radius()

    def update(self, ref_point):
        self.ref_point = ref_point
        self.geometry_points = self.__create_geometry_points(self.geometry_points_cords)
        self.geometry_boundaries = self.__create_geometry_boundaries()

    def __create_geometry_points(self, geometry_points_cords):
        """
        Method that will convert provided geometry points co-ords into named tuples that describe
        geometry on x/y plane
        :param geometry_points_cords:
        :return: geometry_points
        """
        geometry_points = []
        for geometry_cords in geometry_points_cords:
            x = self.ref_point.x + geometry_cords[0]
            y = self.ref_point.y + geometry_cords[1]
            geometry_points.append(Point(x, y))

        return geometry_points

    def __create_geometry_boundaries(self):
        """
        Method that will convert geometry points from class into boundaries created between points
        :return: boundaries
        """
        geometry_points = self.geometry_points

        boundaries = []
        for i in range(len(geometry_points)-1):
            created_boundary = Boundary(geometry_points[i], geometry_points[i+1])
            boundaries.append(created_boundary)

        if self.enclosed_geometry:
            created_boundary = Boundary(geometry_points[-1], geometry_points[0])
            boundaries.append(created_boundary)

        return boundaries

    def __calculate_drag_surfaces(self):
        """
        Method that will calculate drag surfaces in each axis base on geometry
        :return: x_drag_surface, y_drag_surface
        """
        x_cords = []
        y_cords = []
        for single_point in self.geometry_points:
            x_cords.append(single_point.x)
            y_cords.append(single_point.y)

        x_drag_surface = (max(x_cords) - min(x_cords))**2
        y_drag_surface = (max(y_cords) - min(y_cords))**2
        return x_drag_surface, y_drag_surface

    def __calculate_circle_radius(self):
        points_radius = []
        for point in self.geometry_points:
            radius = (point.x ** 2 + point.y ** 2) ** 0.5
            points_radius.append(radius)

        max_radius = max(points_radius)
        return max_radius


if __name__ == "__main__":
    import json
    with open("bullets_config.json", "r") as json_file:
        file = json.load(json_file)
        geometry_cords_file = file["Bullet1"]["geometry"]

    ref_point_ = Point(0, 0)
    geometry = Geometry(ref_point_, geometry_cords_file)
    print(geometry_cords_file)
    for bound in geometry.geometry_boundaries:
        print(bound)
