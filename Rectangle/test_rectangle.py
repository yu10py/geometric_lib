import unittest

from Rectangle.rectangle import area
from Rectangle.rectangle import perimeter

class TestRectangle(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_small_area(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_large_area(self):
        res = area(123456789, 987654321)
        self.assertEqual(res, 121932631112635269)

    def test_square_perimetr(self):
        res = perimeter(20, 20)
        self.assertEqual(res, 80)

    def test_large_perimetr(self):
        res = perimeter(75384901072, 29813745390)
        self.assertEqual(res, 210397292924)

    def test_negative_area(self):
        with self.assertRaises(ValueError):
            res = area(30, -5)

    def test_negative_perimeter(self):
        with self.assertRaises(ValueError):
            res = perimeter(-15, -7)

    def test_string_area(self):
        with self.assertRaises(TypeError):
            res = area("123", "wtf")

    def test_string_perimetr(self):
        with self.assertRaises(TypeError):
            res = area("123", "wtf")