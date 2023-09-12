import unittest
from src.main import Triangle


class MyTestCase(unittest.TestCase):
    def test_triangle_1(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.area(), 6)

    def test_triangle_2(self):
        triangle = Triangle(3, 5, 6)
        self.assertEqual(triangle.area(), 7.483314773547883)

    def test_triangle_3(self):
        triangle = Triangle(5, 12, 13)
        self.assertEqual(triangle.area(), 30)