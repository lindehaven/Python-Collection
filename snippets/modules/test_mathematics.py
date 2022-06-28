'''Test mathematics'''

import unittest
from mathematics import add, sub, mul, div

class TestSuite(unittest.TestCase):
    '''Test suite class containing test cases'''

    def test_add(self):
        '''Test cases for add()'''
        self.assertEqual(add(2.0, 1.0), 3.0)

    def test_sub(self):
        '''Test cases for sub()'''
        self.assertEqual(sub(2.0, 1.0), 1.0)

    def test_mul(self):
        '''Test cases for mul()'''
        self.assertEqual(mul(2.0, 1.0), 2.0)

    def test_div(self):
        '''Test cases for div()'''
        self.assertEqual(div(2.0, 1.0), 2.0)
        self.assertEqual(div(2.0, 0.0), None)

if __name__ == '__main__':
    unittest.main()
