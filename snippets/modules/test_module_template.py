'''Test Module Template

Gives a base for testing Python modules using unittest.
'''
import unittest
from math import pi
from module_template import area, circumference

class TestSuite(unittest.TestCase):
    '''Test suite class containing test cases'''

    def test_area(self):
        '''Test cases for area()'''
        self.assertEqual(area(1.0), pi)

    def test_circumference(self):
        '''Test cases for circumference()'''
        self.assertEqual(circumference(1.0), 2*pi)

if __name__ == '__main__':
    unittest.main()
