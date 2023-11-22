import unittest

from Circle.circle import area
from Circle.circle import perimeter

class TestCircle(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_small_area(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_large_area(self):
        res = area(123456789)
        self.assertEqual(res, 47882831830708840)

    def test_small_perimeter(self):
        res = perimeter(20)
        self.assertEqual(res, 125.66370614359172)

    def test_large_perimeter(self):
        res = perimeter(75384901072)
        self.assertEqual(res, 473657302798.77704)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            res = area(-3)

    def test_negative_perimeter(self):
         with self.assertRaises(ValueError):
            res = perimeter(-5)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            res = area("zhopa")

    def test_string_perimeter(self):
        with self.assertRaises(TypeError):
            res = perimeter("jjk")