from unittest import TestCase
from point import Point
import random


class TestPhysicsSimulation(TestCase):
    def test_point(self):
        range_numbers = 10
        test_cases = 1000
        for _ in range(test_cases):
            a = random.random()*range_numbers-0.5*range_numbers
            b = random.random()*range_numbers-0.5*range_numbers
            test_point = Point(a, b)
            self.assertTrue(test_point.x == a)
            self.assertTrue(test_point.y == b)
