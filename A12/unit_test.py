import unittest
import pandas as pd
import numpy as np
from stats_function import calculate_mean_med
from validate_functions import validate_sex, validate_age

class UnitTest_stats(unittest.TestCase):
    def mean_med_test(self):
        data = pd.Series([10, 20, 30, 40, 50])
        mean, median = calculate_mean_med(data)
        self.assertEqual(mean, np.mean(data))
        self.assertEqual(median, np.median(data))

    def mean_med_edge_case(self):
        data = pd.Series([])
        mean, median = calculate_mean_med(data)
        self.assertIsNone(mean)
        self.assertIsNone(median)

class UnitTest_validate(unittest.TestCase):
    def test_validate_sex_invalid_type(self):
        data = pd.Series(['M', 'F', 101, None])
        result = validate_sex(data)
        self.assertFalse(result)

    def over_age(self):
        data = pd.Series([25, 101, -1, 50])
        result = validate_age(data)
        self.assertFalse(result)

    def correct_age(self):
        data = pd.Series([2, 10, 19, 40])
        result = validate_age(data)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
