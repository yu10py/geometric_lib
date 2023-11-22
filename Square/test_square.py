import unittest

from Square.square import area
from Square.square import perimeter

class TestSquare(unittest.TestCase):
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

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            res = area(-53)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            res = perimeter(-7)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            res = area("123")

    def test_string_perimetr(self):
        with self.assertRaises(TypeError):
            res = area("wtf")