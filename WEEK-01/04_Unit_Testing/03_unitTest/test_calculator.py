
import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(8, 7), 15)

    def test_subtract(self):
        self.assertEqual(subtract(15, 5), 10)

    def test_multiply(self):
        self.assertEqual(multiply(6, 5), 30)

    def test_divide(self):
        self.assertEqual(divide(20, 4), 5)


if __name__ == "__main__":
    unittest.main()