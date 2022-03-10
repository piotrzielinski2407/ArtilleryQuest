from unittest import TestCase
from boundary import Boundary
from point import Point
import random


class TestBoundary(TestCase):
    def test_boundary(self):
        range_numbers = 10
        test_cases = 10000
        for _ in range(test_cases):
            x1 = random.random()*range_numbers-0.5*range_numbers
            y1 = random.random()*range_numbers-0.5*range_numbers
            x2 = random.random()*range_numbers-0.5*range_numbers
            y2 = random.random()*range_numbers-0.5*range_numbers
            test_point1 = Point(x1, y1)
            test_point2 = Point(x2, y2)
            test_boundary = Boundary(test_point1, test_point2)
            if x1 == x2:
                a = None
                b = None
            else:
                a = (y2 - y1) / (x2 - x1)
                b = y1 - a * x1

            self.assertTrue(a == test_boundary.a)
            self.assertTrue(b == test_boundary.b)
            self.assertTrue(x1 == test_boundary.x1)
            self.assertTrue(x2 == test_boundary.x2)
            self.assertTrue(y1 == test_boundary.y1)
            self.assertTrue(y2 == test_boundary.y2)
