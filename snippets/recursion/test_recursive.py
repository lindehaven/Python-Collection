import unittest
import recursive

class TestSuite(unittest.TestCase):

    def test_recursive_factorial(self):
        self.assertEqual(recursive.recursive_factorial(-1), 1)
        self.assertEqual(recursive.recursive_factorial(0), 1)
        self.assertEqual(recursive.recursive_factorial(1), 1)
        self.assertEqual(recursive.recursive_factorial(2), 2)
        self.assertEqual(recursive.recursive_factorial(3), 6)
        self.assertEqual(recursive.recursive_factorial(4), 24)
        self.assertEqual(recursive.recursive_factorial(5), 120)
        self.assertEqual(recursive.recursive_factorial(6), 720)

    def test_for_factorial(self):
        self.assertEqual(recursive.for_factorial(-1), 1)
        self.assertEqual(recursive.for_factorial(0), 1)
        self.assertEqual(recursive.for_factorial(1), 1)
        self.assertEqual(recursive.for_factorial(2), 2)
        self.assertEqual(recursive.for_factorial(3), 6)
        self.assertEqual(recursive.for_factorial(4), 24)
        self.assertEqual(recursive.for_factorial(5), 120)
        self.assertEqual(recursive.for_factorial(6), 720)

    def test_while_factorial(self):
        self.assertEqual(recursive.while_factorial(-1), 1)
        self.assertEqual(recursive.while_factorial(0), 1)
        self.assertEqual(recursive.while_factorial(1), 1)
        self.assertEqual(recursive.while_factorial(2), 2)
        self.assertEqual(recursive.while_factorial(3), 6)
        self.assertEqual(recursive.while_factorial(4), 24)
        self.assertEqual(recursive.while_factorial(5), 120)
        self.assertEqual(recursive.while_factorial(6), 720)

if __name__ == '__main__':
    unittest.main()
