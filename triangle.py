import unittest


def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c


class TestTriangle(unittest.TestCase):

    def test_area_positive_values(self):
        self.assertEqual(area(10, 5), 25)
        self.assertEqual(area(4, 3), 6)

    def test_area_zero(self):
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)

    def test_area_float_values(self):
        self.assertEqual(area(2.5, 4), 5.0)

    def test_perimeter_positive_values(self):
        self.assertEqual(perimeter(3, 4, 5), 12)
        self.assertEqual(perimeter(1, 1, 1), 3)

    def test_perimeter_zero_values(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_float_values(self):
        self.assertEqual(perimeter(2.5, 3.5, 4), 10.0)


if __name__ == "__main__":
    unittest.main()
