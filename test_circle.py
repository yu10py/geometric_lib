import math
import unittest

from circle import area
from circle import perimeter

res = '{:.0f}'.format(2 * 20 * math.pi)
print(res)

class TestRectangle(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_small_area(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_large_area(self):
        res = area(123456789)
        self.assertEqual(res, 47882831830708840)

    def test_small_perimetr(self):
        res = perimeter(20)
        self.assertEqual(res, 125.66370614359172)

    def test_large_perimetr(self):
        res = perimeter(75384901072)
        self.assertEqual(res, 473657302798.77704)