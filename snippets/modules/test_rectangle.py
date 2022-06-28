'''Test rectangle'''

import unittest
from rectangle import area, circ

class TestSuite(unittest.TestCase):
    '''Test suite class containing test cases'''

    def test_area(self):
        '''Test cases for area()'''
        self.assertEqual(area(1.0, 1.0), 1.0)

    def test_circ(self):
        '''Test cases for circumference()'''
        self.assertEqual(circ(1.0, 1.0), 4.0)

if __name__ == '__main__':
    unittest.main()
