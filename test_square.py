import unittest

from square import area
from square import perimeter

class TestRectangle(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_small_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_large_area(self):
        res = area(29813745390)
        self.assertEqual(res, 888859414179746252100)

    def test_square_perimetr(self):
        res = perimeter(20)
        self.assertEqual(res, 80)

    def test_large_perimetr(self):
        res = perimeter(973165903242)
        self.assertEqual(res, 3892663612968)