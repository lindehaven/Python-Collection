'''Energy Unit (CU) Test Module

Author : Lars Lindehaven
Date   : 2019-06-05
'''
# pylint: disable=protected-access

import unittest
import obceu

class TestSuiteBasic(unittest.TestCase):
    '''Test suite class containing basic test cases'''

    def setUp(self):
        '''Setup for test cases'''
        obceu.charge_battery_energy(100)

    def test_sampled(self):
        '''Test cases for _sampled()'''
        self.assertTrue(obceu._sampled(0.1, 0.0, 0.0, 0.0, 0.0))
        self.assertTrue(obceu._sampled(0.1, 1.0, 1.0, 1.0, 1.0))
        self.assertTrue(obceu._sampled(0.1, -1.0, -1.0, -1.0, -1.0))
        obceu.charge_battery_energy(0)
        self.assertFalse(obceu._sampled(0.1, 0.0, 0.0, 0.0, 0.0))

    def test_charge_battery_energy(self):
        '''Test cases for charge_battery_energy()'''
        self.assertFalse(obceu.charge_battery_energy(-1))
        self.assertFalse(obceu.charge_battery_energy(101))
        self.assertTrue(obceu.charge_battery_energy(100))

    def test_maximum_battery_energy(self):
        '''Test cases for maximum_battery_energy()'''
        self.assertAlmostEqual(obceu.maximum_battery_energy(),
                               obceu._MAX_BATTERY_CAPACITY)

    def test_remaining_battery_energy(self):
        '''Test cases for remaining_battery_energy()'''
        self.assertAlmostEqual(obceu.remaining_battery_energy(),
                               100/100*obceu._MAX_BATTERY_CAPACITY)
        self.assertTrue(obceu.charge_battery_energy(1))
        self.assertAlmostEqual(obceu.remaining_battery_energy(),
                               1/100*obceu._MAX_BATTERY_CAPACITY)
        self.assertTrue(obceu.charge_battery_energy(0.1))
        self.assertAlmostEqual(obceu.remaining_battery_energy(),
                               0.1/100*obceu._MAX_BATTERY_CAPACITY)


if __name__ == '__main__':
    unittest.main()
