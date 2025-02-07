from unittest import TestCase
from functions import divide, multiply


class TestFuctions(TestCase):
    def test_divide_result(self):
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(25, 0)
        # Could write it like below, but it's probably less clear.
        # self.assertRaises(ValueError, lambda: divide(25, 0))

    def test_multiply_empty(self):
        with self.assertRaises(ValueError):
            multiply()
    
    def test_multiply_single_value(self):
        expected = 15
        self.assertEqual(multiply(expected), expected)
    
    def test_multiply_just_zero(self):
        expected = 0
        self.assertEqual(multiply(expected), expected)
    
    def test_multiply_result(self):
        inputs = (3, 7)
        expected = 21
        self.assertEqual(multiply(*inputs), expected)
    
    def test_multiply_by_zero(self):
        inputs = (3, 7, 0)
        expected = 0
        self.assertEqual(multiply(*inputs), expected)
    
    def test_multiply_single_negative(self):
        inputs = (3, -7, 5)
        expected = -105
        self.assertEqual(multiply(*inputs), expected)
    
    def test_multiply_double_negative(self):
        inputs = (3, -7, -5)
        expected = 105
        self.assertEqual(multiply(*inputs), expected)

    def test_multiply_floats(self):
        inputs = (3.2, 7.0)
        expected = 22.4
        self.assertAlmostEqual(multiply(*inputs), expected)
