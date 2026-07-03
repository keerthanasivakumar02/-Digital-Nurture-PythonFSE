import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(8, 2), 10)

    def test_subtract(self):
        self.assertEqual(subtract(12, 5), 7)

    def test_multiply(self):
        self.assertEqual(multiply(4, 6), 24)

    def test_divide(self):
        self.assertEqual(divide(20, 4), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()