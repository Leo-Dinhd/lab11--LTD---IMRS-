# https://github.com/Leo-Dinhd/lab11--LTD---IMRS-
# Partner 1: Leo Dinh
# Partner 2: Isaac Reyes
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Isaac Reyes
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-2, -3), -5)

    ######## Leo Dinh
    def test_multiply(self):  # 3 assertions
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-3, 4), -12)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):  # 3 assertions
        # divide(a, b) is b / a
        self.assertEqual(divide(2, 10), 5)
        self.assertEqual(divide(-2, 10), -5)
        self.assertAlmostEqual(divide(3, 1), 1 / 3)
    # ##########################

  ######## Isaac Reyes 
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)

   def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(8, 2), 3.0)
        self.assertAlmostEqual(logarithm(9, 3), 2.0)
        self.assertAlmostEqual(logarithm(100, 10), 2.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 1)
    
    ######## Isaac Reyes
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)
        self.assertAlmostEqual(hypotenuse(1, 1), 2 ** 0.5)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertAlmostEqual(square_root(2), 2 ** 0.5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
