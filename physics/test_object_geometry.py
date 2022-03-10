from unittest import TestCase
from geometry import Geometry
from point import Point
from boundary import Boundary

test_stack = [[-1, 1], [1, 1], [1, -1], [-1, -1]]
result_surfaces = [4, 4]
ref_point = Point(1, 4)
class_instance = Geometry(ref_point, test_stack)


class TestGeometry(TestCase):

    def test_create_geometry(self):
        result = class_instance.geometry_points
        expected_value = [Point(element[0]+ref_point.x, element[1]+ref_point.y) for element in test_stack]

        self.assertTrue(result == expected_value)
        for point_in_class in result:
            self.assertTrue(isinstance(point_in_class, Point))
            self.assertTrue(isinstance(point_in_class.x, int))
            self.assertTrue(isinstance(point_in_class.y, int))

    def test_calculate_drag_surfaces(self):
        result1 = class_instance.x_drag_surface
        result2 = class_instance.y_drag_surface
        expected_value_1 = result_surfaces[0]
        expected_value_2 = result_surfaces[1]

        self.assertEqual(result1, expected_value_1)
        self.assertEqual(result2, expected_value_2)

    def test_create_geometry_boundaries(self):
        for boundary in class_instance.geometry_boundaries:
            self.assertTrue(isinstance(boundary, Boundary))
            if boundary.x1 == boundary.x2:
                self.assertEqual(boundary.a, None)
                self.assertEqual(boundary.b, None)
            else:
                a = (boundary.y2 - boundary.y1) / (boundary.x2 - boundary.x1)
                b = boundary.y1 - a * boundary.x1
                self.assertEqual(boundary.a, a)
                self.assertEqual(boundary.b, b)
            if class_instance.enclosed_geometry:
                self.assertEqual(len(class_instance.geometry_boundaries), len(test_stack))
            else:
                self.assertEqual(len(class_instance.geometry_boundaries), len(test_stack)-1)
