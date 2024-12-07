import unittest
from math_functions import pow, div 

class UnitTest(unittest.TestCase):

    def positive_num(self):
        self.assertEqual(pow(2, 10), 1024)  

    def zero(self):
        self.assertEqual(pow(2, 0), 1)

    def negative_num(self):
        self.assertAlmostEqual(pow(2, -2), 0.25)

    def positive_num_div(self):
        self.assertEqual(div(100, 10), 10)

    def zero_num_div(self):
        with self.assertRaises(ValueError):
            div(50, 0)

    def negative_num_div(self):
        self.assertEqual(div(-3, 3), -1)

if __name__ == "__main__":
    unittest.main()

