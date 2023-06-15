import unittest
from ('6-max_integer.py') import max_integer

"""
test for Max integer - Unittest
"""
class TestMaxinteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_item(self):
        self.assertEqual(max_integer([10]), 10)

    def test_zero(self):
        self.assertEqual(max_integer([0]), 0)

    def test_integers(self):
        self.assertEqual(max_integer([2, 4, 9]), 9)

    def test_negative_number(self):
        self.assertEqual(max_integer([-3, -20, -5, -1]), -1)

    def test_negative_positive(self):
        self.assertEqual(max_integer([-1, 6.2, 9]), 9)

    def test_floating_numbers(self):
        self.assertEqual(max_integer([0.6, 4.8, 8.7]), 8.7)

    def test_non_value(self):
        self.assertEqual(max_integer([7, 8, x]), 8)

if __name__ == '__main__':
    unittest.main()
