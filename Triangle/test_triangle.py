import unittest

from Triangle.triangle import area
from Triangle.triangle import perimeter

class TestTriangle(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_zero_area_2(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_large_area(self):
        res = area(5879324522, 134513256136)
        self.assertEqual(res, 395423542667225858048)

    def test_large_perimetr(self):
        res = perimeter(7852134593240, 481325073680324, 5329679326862463)
        self.assertEqual(res, 5818856535136027)

    def test_small_perimetr(self):
        res = perimeter(1, 0, 34)
        self.assertEqual(res, 35)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            res = area(30, -5)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            res = perimeter(34, -15, -7)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            res = area("123", "wtf")

    def test_string_perimetr(self):
        with self.assertRaises(TypeError):
            res = area("123", "wtf", "AAAAAA")