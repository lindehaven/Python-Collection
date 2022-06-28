'''Test circle'''

import unittest
from math import pi
from circle import area, circ

class TestSuite(unittest.TestCase):
    '''Test suite class containing test cases'''

    def test_area(self):
        '''Test cases for area()'''
        self.assertEqual(area(1.0), 1.0*pi)

    def test_circ(self):
        '''Test cases for circumference()'''
        self.assertEqual(circ(1.0), 2.0*pi)

if __name__ == '__main__':
    unittest.main()
