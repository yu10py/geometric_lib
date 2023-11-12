import unittest

from triangle import area
from triangle import perimeter

print('{:.0f}'.format(7852134593240 + 481325073680324 + 5329679326862463))

class TestRectangle(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_zero_area_2(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_large_area(self):
        res = area(5879324522, 134513256136);
        self.assertEqual(res, 395423542667225858048)

    def test_large_perimetr(self):
        res = perimeter(7852134593240, 481325073680324, 5329679326862463)
        self.assertEqual(res, 5818856535136027)

    def test_small_perimetr(self):
        res = perimeter(1, 0 ,34)
        self.assertEqual(res, 35)