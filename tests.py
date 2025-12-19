import unittest
import math

from triangle import area as triangle_area, perimeter as triangle_perimeter
from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter


class TestTriangle(unittest.TestCase):

    def test_triangle_area(self):
        self.assertEqual(triangle_area(10, 5), 25)
        self.assertEqual(triangle_area(0, 5), 0)

    def test_triangle_perimeter(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)


class TestCircle(unittest.TestCase):

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(2), 4 * math.pi)

    def test_circle_perimeter(self):
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(2), 4 * math.pi)


class TestRectangle(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(3, 4), 12)
        self.assertEqual(rectangle_area(0, 5), 0)

    def test_rectangle_perimeter(self):
        self.assertEqual(rectangle_perimeter(3, 4), 7)


class TestSquare(unittest.TestCase):

    def test_square_area(self):
        self.assertEqual(square_area(4), 16)
        self.assertEqual(square_area(0), 0)

    def test_square_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)


if __name__ == "__main__":
    unittest.main()
