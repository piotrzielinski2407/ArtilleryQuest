from unittest import TestCase
from simulation import PhysicsSimulation
from boundary import Boundary
from point import Point
from physical_object import UniversalPhysicalObject
from geometry import Geometry

test_time_scale = 0.001
test_gravity = 9.8065
test_density = 1.1


class TestPhysicsSimulation(TestCase):

    def test_check_boundary_collision(self):
        test_stack = [
            [Boundary(Point(0, 0), Point(0, 0)), Boundary(Point(0, 0), Point(0, 0)), True],
            [Boundary(Point(-2, -2), Point(2, 2)), Boundary(Point(-2, 2), Point(2, -2)), True],
            [Boundary(Point(-2, -2), Point(-1, -1)), Boundary(Point(-2, 2), Point(-1, 1)), False],
            [Boundary(Point(-2, 0), Point(-2, 5)), Boundary(Point(-2, -5), Point(-2, -3)), False],
            [Boundary(Point(-2, 0), Point(-2, 5)), Boundary(Point(-2, -2), Point(-2, 2)), True],
            [Boundary(Point(0, -5), Point(0, 5)), Boundary(Point(-2, -2), Point(2, 2)), True],
            [Boundary(Point(-2, -2), Point(2, 2)), Boundary(Point(0, -5), Point(0, 5)), True],
            [Boundary(Point(-5, 5), Point(5, 5)), Boundary(Point(0, 0), Point(0, 10)), True],
            [Boundary(Point(-5, 5), Point(-5, 5)), Boundary(Point(-5, 2), Point(-5, 2)), False],
            [Boundary(Point(-5, 5), Point(5, 5)), Boundary(Point(-5, 5), Point(5, 5)), True]]
        test_object = PhysicsSimulation(test_time_scale, test_gravity, test_density)
        for test_pack in test_stack:
            boundary1 = test_pack[0]
            boundary2 = test_pack[1]
            result_expected = test_pack[2]
            result = test_object.check_boundary_collision(boundary1, boundary2)
            self.assertTrue(result == result_expected)

    def test_check_objects_collision(self):
        geometry1_cords = [[0, 0], [0, 3], [3, 3], [3, 0]]
        geometry2_cords = [[1, 1], [1, 4], [4, 4], [4, 1]]
        geometry3_cords = [[6, 6], [6, 7], [7, 7], [7, 6]]

        ref_point_ = Point(0, 0)

        object1 = UniversalPhysicalObject()
        object1.geometry = Geometry(ref_point_, geometry1_cords)
        object2 = UniversalPhysicalObject()
        object2.geometry = Geometry(ref_point_, geometry2_cords)
        object3 = UniversalPhysicalObject()
        object3.geometry = Geometry(ref_point_, geometry3_cords)

        test_stack = [[object1, object2, True],
                      [object1, object3, False],
                      [object2, object3, False]]
        test_object = PhysicsSimulation(test_time_scale, test_gravity, test_density)

        for test_pack in test_stack:
            test_object1 = test_pack[0]
            test_object2 = test_pack[1]
            result_expected = test_pack[2]
            result = test_object.check_objects_collision(test_object1, test_object2)
            self.assertTrue(result == result_expected)

    def test_check_collision(self):
        geometry1_cords = [[0, 0], [0, 3], [3, 3], [3, 0]]
        geometry2_cords = [[1, 1], [1, 4], [4, 4], [4, 1]]
        geometry3_cords = [[6, 6], [6, 7], [7, 7], [7, 6]]

        ref_point_ = Point(0, 0)

        object1 = UniversalPhysicalObject()
        object1.geometry = Geometry(ref_point_, geometry1_cords)
        object1.status = False
        object1.colision_dependent = True
        object2 = UniversalPhysicalObject()
        object2.geometry = Geometry(ref_point_, geometry2_cords)
        object2.status = False
        object2.colision_dependent = True
        object3 = UniversalPhysicalObject()
        object3.geometry = Geometry(ref_point_, geometry3_cords)
        object3.status = False
        object3.colision_dependent = True

        test_object = PhysicsSimulation(test_time_scale, test_gravity, test_density)
        test_object.add_object(object1)
        test_object.add_object(object2)
        test_object.add_object(object3)
        test_object.check_collisions()

        self.assertTrue(object1.status is False)
        self.assertTrue(object2.status is False)
        self.assertTrue(object3.status is True)
