from unittest import TestCase
from objects_physics import PhysicsSimulation
from boundary import Boundary
from point import Point

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
            [Boundary(Point(-5, 5), Point(-5, 5)), Boundary(Point(-5, 2), Point(-5, 2)), False]
        ]
        test_object = PhysicsSimulation(test_time_scale, test_gravity, test_density)
        for test_pack in test_stack:
            boundary1 = test_pack[0]
            boundary2 = test_pack[1]
            result_expected = test_pack[2]
            result = test_object.check_boundary_collision(boundary1, boundary2)
            print(boundary1, boundary2, result_expected, result)
            self.assertTrue(result == result_expected)
