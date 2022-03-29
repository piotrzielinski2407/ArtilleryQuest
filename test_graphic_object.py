from unittest import TestCase
from graphic_object import UniversalGraphicObject
from geometry import Geometry
from point import Point
boundary_color = 'red'
line_thickness = 2
fill_color = 'red'
fill = True


class TestUniversalGraphicObject(TestCase):
    def test_return_graphic_chunk(self):
        start_point = Point(0, 0)
        geometry_points = [[0, 0], [0, 1], [1, 1], [1, 0]]
        geometry_object = Geometry(start_point, geometry_points)
        graphic_object = UniversalGraphicObject()
        graphic_object.geometry = geometry_object
        graphic_object.boundary_color = boundary_color
        graphic_object.boundary_thickness = line_thickness
        graphic_object.fill_color = fill_color
        graphic_object.fill_object = True
        graphic_object.status = True
        graphic_object.explode_on_hit = True
        test_chunk = graphic_object.return_graphic_chunk()

        self.assertTrue(test_chunk['fill'] == fill)
        self.assertTrue(test_chunk['thickness'] == line_thickness)
        self.assertTrue(test_chunk['colors']['boundary'] == boundary_color)
        self.assertTrue(test_chunk['colors']['fill'] == fill_color)
        self.assertTrue(isinstance(test_chunk['geometry'], Geometry))
        self.assertTrue(test_chunk['status'] is True)
        self.assertTrue(test_chunk['collision'] is True)


