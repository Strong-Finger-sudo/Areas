import unittest
from src.main import Circle

class TestCircleArea(unittest.TestCase):
    def test_circle_area_1(self):
        circle = Circle(5)
        self.assertEqual(circle.area(), 78.5)

    def test_circle_area_2(self):
        assert Circle(1).area() == 3.14


    def test_circle_area_3(self):
        assert Circle(2).area() == 12.56