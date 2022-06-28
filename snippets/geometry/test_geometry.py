import unittest
from geometry import rectangle_area, rectangle_circ, rectangle_aspect

class TestSuite(unittest.TestCase):
    def test_rektangel(self):
        self.assertEqual(rectangle_area(2.0, 3.0), 6.0)
        self.assertEqual(rectangle_area(0.0, 3.0), 0.0)
        self.assertEqual(rectangle_area(-2.0, 3.0), 6.0)
        self.assertEqual(rectangle_circ(2.0, 3.0), 10.0)
        self.assertEqual(rectangle_circ(0.0, 0.0), 0.0)
        self.assertEqual(rectangle_circ(-2.0, 3.0), 10.0)
        self.assertEqual(rectangle_aspect(3.0, 2.0), 1.5)
        self.assertEqual(rectangle_aspect(-3.0, -2.0), 1.5)
        self.assertEqual(rectangle_aspect(0.0, 2.0), 0.0)
        self.assertEqual(rectangle_aspect(3.0, 0.0), 0.0)

if __name__ == '__main__':
    unittest.main()
