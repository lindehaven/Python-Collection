import unittest
import module as m

class TestSuite(unittest.TestCase):

    def test_functions(self):

        self.assertEqual(m.my_min(1, 2, 3), 1)
        self.assertEqual(m.my_min(2.3, 3.4, 1.2), 1.2)
        self.assertEqual(m.my_min(0, 0, 0), 0)
        self.assertEqual(m.my_min(-3, -2, -1), -3)

        self.assertEqual(m.my_max(1, 2, 3), 3)
        self.assertEqual(m.my_max(2.3, 3.4, 1.2), 3.4)
        self.assertEqual(m.my_max(0, 0, 0), 0)
        self.assertEqual(m.my_max(-3, -2, -1), -1)

        self.assertEqual(m.my_mean(1, 2, 3), 2)
        self.assertEqual(m.my_mean(2.3, 3.4, 1.2), 2.3)
        self.assertEqual(m.my_mean(0, 0, 0), 0)
        self.assertEqual(m.my_mean(-3, -2, -1), -2)

        self.assertEqual(m.my_median(1, 2, 3), 2)
        self.assertEqual(m.my_median(2.3, 3.4, 1.2), 2.3)
        self.assertEqual(m.my_median(0, 0, 0), 0)
        self.assertEqual(m.my_median(-3, -2, -1), -2)

    def test_list_functions(self):

        self.assertEqual(m.my_list_min([1, 2, 3]), 1)
        self.assertEqual(m.my_list_min([2.3, 3.4, 1.2]), 1.2)
        self.assertEqual(m.my_list_min([0, 0, 0]), 0)
        self.assertEqual(m.my_list_min([-3, -2, -1]), -3)
        self.assertEqual(m.my_list_min([]), None)

        self.assertEqual(m.my_list_max([1, 2, 3]), 3)
        self.assertEqual(m.my_list_max([2.3, 3.4, 1.2]), 3.4)
        self.assertEqual(m.my_list_max([0, 0, 0]), 0)
        self.assertEqual(m.my_list_max([-3, -2, -1]), -1)
        self.assertEqual(m.my_list_max([]), None)

        self.assertEqual(m.my_list_mean([1, 2, 3]), 2)
        self.assertEqual(m.my_list_mean([2.3, 3.4, 1.2]), 2.3)
        self.assertEqual(m.my_list_mean([0, 0, 0]), 0)
        self.assertEqual(m.my_list_mean([-3, -2, -1]), -2)
        self.assertEqual(m.my_list_mean([1, 3, 2, 6]), 3)
        self.assertEqual(m.my_list_mean([]), None)

        self.assertEqual(m.my_list_median([1, 2, 3]), 2)
        self.assertEqual(m.my_list_median([1.2, 2.3, 3.4]), 2.3)
        self.assertEqual(m.my_list_median([0, 0, 0]), 0)
        self.assertEqual(m.my_list_median([-3, -2, -1]), -2)
        self.assertEqual(m.my_list_median([6, 1, 3, 2]), 2.5)

        self.assertEqual(m.my_list_median([]), None)
        self.assertEqual(m.my_list_median([1]), 1)
        self.assertEqual(m.my_list_median([1, 2]), 1.5)
        self.assertEqual(m.my_list_median([3, 2, 1, 1, 1, 1, 2, 3]), 1.5)

if __name__ == '__main__':
    unittest.main()
