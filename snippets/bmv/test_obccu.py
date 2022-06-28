'''Calculation Unit (CU) Test Module

Author : Lars Lindehaven
Date   : 2019-06-05
'''
# pylint: disable=no-self-use,protected-access,too-many-arguments

# Imports
import unittest
import obccu
import obceu


class TestSuiteBasic(unittest.TestCase):
    '''Test suite class containing basic test cases'''

    def setUp(self):
        '''Setup for test cases'''
        obceu.charge_battery_energy(100.0)

    def sampled(self, tsps, flwd, frwd, rlwd, rrwd):
        '''Calls both sampled() functions'''
        outcome = False
        if obceu._sampled(tsps, flwd, frwd, rlwd, rrwd):
            outcome = obccu.sampled(tsps, flwd, frwd, rlwd, rrwd)
        return outcome

    def test_sampled(self):
        '''Test cases for sampled()'''
        if obccu.sampled(0.1, 0, 0, 0, 0) is not None:
            # Forward
            self.assertTrue(obccu.sampled(0.1, 0, 0, 0, 0))
            self.assertTrue(obccu.sampled(0.1, 1, 1, 1, 1))
            self.assertTrue(obccu.sampled(1, 1, 1, 1, 1))
            # Reverse
            self.assertTrue(obccu.sampled(0.1, -1, -1, -1, -1))
            self.assertTrue(obccu.sampled(1, -1, -1, -1, -1))

    def test_travelled_distance(self):
        '''Test cases for travelled_distance()'''
        if obccu.travelled_distance() is not None:
            self.sampled(0.1, 0, 0, 0, 0)
            dist = obccu.travelled_distance()
            # 1000 meters forward
            self.sampled(60, 1_000, 1_000, 1_000, 1_000)
            self.assertAlmostEqual(obccu.travelled_distance(), dist + 1_000)
            # 100 meters backward
            self.sampled(60, -100, -100, -100, -100)
            self.assertAlmostEqual(obccu.travelled_distance(), dist + 1_100)

    def test_current_speed(self):
        '''Test cases for current_speed()'''
        if obccu.current_speed() is not None:
            self.sampled(0.1, 1.0, 1.0, 1.0, 1.0)
            self.assertAlmostEqual(obccu.current_speed(), 36.0)
            self.sampled(0.1, 2.0, 2.0, 2.0, 2.0)
            self.assertAlmostEqual(obccu.current_speed(), 72.0)
            self.sampled(0.1, 2.5, 2.5, 2.5, 2.5)
            self.assertAlmostEqual(obccu.current_speed(), 90.0)

    def test_average_speed(self):
        '''Test cases for average_speed()'''
        if obccu.average_speed() is not None:
            self.sampled(0.1, 1.0, 1.0, 1.0, 1.0)
            average_speed = obccu.average_speed()
            dist = average_speed / 36.0
            self.sampled(0.1, dist, dist, dist, dist)
            self.assertEqual(obccu.average_speed(), average_speed)
            for _ in range(50):
                self.sampled(0.1, dist/2, dist/2, dist/2, dist/2)
            self.assertTrue(obccu.average_speed() <= average_speed)
            for _ in range(50):
                self.sampled(0.1, dist*3, dist*3, dist*3, dist*3)
            self.assertTrue(obccu.average_speed() >= average_speed)

    def test_average_power_consumption(self):
        '''Test cases for average_power_consumption()'''
        if obccu.average_power_consumption() is not None:
            self.assertEqual(obccu.average_power_consumption(), 0)
            for _ in range(50):
                self.sampled(0.1, 2.5, 2.5, 2.5, 2.5)
            self.assertTrue(obccu.average_power_consumption() >= 8)
            for _ in range(50):
                self.sampled(0.1, 5.0, 5.0, 5.0, 5.0)
            self.assertTrue(obccu.average_power_consumption() >= 10)
            for _ in range(50):
                self.sampled(0.1, 7.5, 7.5, 7.5, 7.5)
            self.assertTrue(obccu.average_power_consumption() >= 13)

    def test_remaining_distance(self):
        '''Test cases for remaining_distance()'''
        if obccu.remaining_distance() is not None:
            remaining_distance = obccu.remaining_distance()
            self.assertEqual(obccu.remaining_distance(), remaining_distance)
            for _ in range(50):
                self.sampled(0.1, 10, 10, 10, 10)
            self.assertTrue(obccu.remaining_distance() < remaining_distance)

    def test_wheel_skid_warning(self):
        '''Test cases for wheel_skid_warning()'''
        if obccu.wheel_skid_warning() is not None:
            self.sampled(0.1, 2.0, 2.0, 2.0, 2.0)
            # Constant speed
            self.sampled(0.1, 2.0, 2.0, 2.0, 2.0)
            self.assertFalse(obccu.wheel_skid_warning())
            # Skidding             no        no  (1.3 > 1.5/1.5)
            self.sampled(0.1, 1.5, 1.3, 1.5, 1.3)
            self.assertFalse(obccu.wheel_skid_warning())
            # Skidding             no        yes (0.8 < 1.4/1.5)
            self.sampled(0.1, 1.4, 1.2, 1.4, 0.8)
            self.assertTrue(obccu.wheel_skid_warning())
            # Skidding             no        no  (1.3 > 1.3/1.5)
            self.sampled(0.1, 1.3, 1.3, 1.3, 1.3)
            self.assertFalse(obccu.wheel_skid_warning())
            self.sampled(0.1, 1.3, 1.3, 1.3, 1.3)
            self.assertFalse(obccu.wheel_skid_warning())

    def test_wheel_spin_warning(self):
        '''Test cases for wheel_spin_warning()'''
        if obccu.wheel_spin_warning() is not None:
            self.sampled(0.1, 1.0, 1.0, 1.0, 1.0)
            # Constant speed
            self.sampled(0.1, 1.0, 1.0, 1.0, 1.0)
            self.assertFalse(obccu.wheel_spin_warning())
            # Spinning        no        no  (2.6 < 1.8*1.5)
            self.sampled(0.1, 2.0, 1.8, 2.6, 1.8)
            self.assertFalse(obccu.wheel_spin_warning())
            # Spinning        no        yes (2.8 > 1.8*1.5)
            self.sampled(0.1, 2.0, 1.8, 2.8, 1.8)
            self.assertTrue(obccu.wheel_spin_warning())
            # Spinning        no        no  (2.2 < 2.2*1.5)
            self.sampled(0.1, 2.2, 2.2, 2.2, 2.2)
            self.assertFalse(obccu.wheel_spin_warning())
            self.sampled(0.1, 2.2, 2.2, 2.2, 2.2)
            self.assertFalse(obccu.wheel_spin_warning())


class TestSuiteTough(unittest.TestCase):
    '''Test suite class containing tough test cases'''

    def setUp(self):
        '''Setup for test cases'''
        obceu.charge_battery_energy(100.0)

    def sampled(self, tsps, flwd, frwd, rlwd, rrwd):
        '''Calls both sampled() functions'''
        outcome = False
        if obceu._sampled(tsps, flwd, frwd, rlwd, rrwd):
            outcome = obccu.sampled(tsps, flwd, frwd, rlwd, rrwd)
        return outcome

    def test_sampled(self):
        '''Test cases for sampled()'''
        if obccu.sampled(0.1, 0, 0, 0, 0) is not None:
            # Lost track of time
            self.assertFalse(obccu.sampled(-0.1, 0, 0, 0, 0))
            self.assertFalse(obccu.sampled(0.0, 0, 0, 0, 0))
            self.assertFalse(obccu.sampled(0.0, 1, 1, 1, 1))

    def test_travelled_distance(self):
        '''Test cases for travelled_distance()'''
        if obccu.travelled_distance() is not None:
            self.sampled(0.1, 0, 0, 0, 0)
            dist = obccu.travelled_distance()
            # 1000 meters backward
            self.sampled(60, -1_000, -1_000, -1_000, -1_000)
            self.assertAlmostEqual(obccu.travelled_distance(), dist + 1_000)
            # 100 meters backward
            self.sampled(60, -100, -100, -100, -100)
            self.assertAlmostEqual(obccu.travelled_distance(), dist + 1_100)

    def test_current_speed(self):
        '''Test cases for current_speed()'''
        if obccu.current_speed() is not None:
            self.sampled(0.1, -1.0, -1.0, -1.0, -1.0)
            self.assertAlmostEqual(obccu.current_speed(), 36.0)
            self.sampled(0.2, -2.5, -2.5, -2.5, -2.5)
            self.assertAlmostEqual(obccu.current_speed(), 45.0)
            self.sampled(0.3, -1.0, -1.0, -1.0, -1.0)
            self.assertAlmostEqual(obccu.current_speed(), 12.0)

    def test_average_speed(self):
        '''Test cases for average_speed()'''
        if obccu.average_speed() is not None:
            self.sampled(0.1, 1.0, 1.0, 1.0, 1.0)
            average_speed = obccu.average_speed()
            dist = average_speed / 36.0
            self.sampled(0.1, dist, dist, dist, dist)
            self.assertEqual(obccu.average_speed(), average_speed)
            for _ in range(50):
                self.sampled(0.1, dist/2, dist/2, dist/2, dist/2)
            self.assertTrue(obccu.average_speed() <= average_speed)
            for _ in range(50):
                self.sampled(0.1, dist*3, dist*3, dist*3, dist*3)
            self.assertTrue(obccu.average_speed() >= average_speed)

    def test_average_power_consumption(self):
        '''Test cases for average_power_consumption()'''
        if obccu.average_power_consumption() is not None:
            self.assertTrue(obccu.average_power_consumption() >= 0)
            for _ in range(50):
                self.sampled(0.1, 2.5, 2.5, 2.5, 2.5)
            self.assertTrue(obccu.average_power_consumption() >= 8)
            for _ in range(50):
                self.sampled(0.1, 5.0, 5.0, 5.0, 5.0)
            self.assertTrue(obccu.average_power_consumption() >= 10)
            for _ in range(50):
                self.sampled(0.1, 7.5, 7.5, 7.5, 7.5)
            self.assertTrue(obccu.average_power_consumption() >= 13)

    def test_remaining_distance(self):
        '''Test cases for remaining_distance()'''
        if obccu.remaining_distance() is not None:
            remaining_distance = obccu.remaining_distance()
            self.assertEqual(obccu.remaining_distance(), remaining_distance)
            for _ in range(50):
                self.sampled(0.1, 10, 10, 10, 10)
            self.assertTrue(obccu.remaining_distance() < remaining_distance)

    def test_wheel_skid_warning(self):
        '''Test cases for wheel_skid_warning()'''
        if obccu.wheel_skid_warning() is not None:
            self.sampled(0.1, 2.0, 2.0, 2.0, 2.0)
            # Constant speed
            self.sampled(0.1, 2.0, 2.0, 2.0, 2.0)
            self.assertFalse(obccu.wheel_skid_warning())
            # Skidding             no        no  (1.3 > 1.5/1.5)
            self.sampled(0.1, 1.5, 1.3, 1.5, 1.3)
            self.assertFalse(obccu.wheel_skid_warning())
            # Skidding             no        yes (0.8 < 1.4/1.5)
            self.sampled(0.1, 1.4, 1.2, 1.4, 0.8)
            self.assertTrue(obccu.wheel_skid_warning())

    def test_wheel_spin_warning(self):
        '''Test cases for wheel_spin_warning()'''
        if obccu.wheel_spin_warning() is not None:
            self.sampled(0.1, 1.0, 1.0, 1.0, 1.0)
            # Constant speed
            self.sampled(0.1, 1.0, 1.0, 1.0, 1.0)
            self.assertFalse(obccu.wheel_spin_warning())
            # Spinning        no        no  (2.6 < 1.8*1.5)
            self.sampled(0.1, 2.0, 1.8, 2.6, 1.8)
            self.assertFalse(obccu.wheel_spin_warning())
            # Spinning        no        yes (2.8 > 1.8*1.5)
            self.sampled(0.1, 2.0, 1.8, 2.8, 1.8)
            self.assertTrue(obccu.wheel_spin_warning())


if __name__ == '__main__':
    unittest.main()
