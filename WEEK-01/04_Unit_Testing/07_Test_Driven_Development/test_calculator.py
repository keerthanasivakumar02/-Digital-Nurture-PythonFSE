import unittest
from calculator import add


class TestCalculator(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add(8, 12), 20)

    def test_add_zero(self):
        self.assertEqual(add(0, 10), 10)

    def test_add_negative(self):
        self.assertEqual(add(-4, 4), 0)


if __name__ == "__main__":
    unittest.main()