import unittest
from main import calculate

class TestCalculate(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate(7, 2, "add"), 9)
        self.assertEqual(calculate(0, 6, "add"), 6)
        self.assertEqual(calculate(-3, 3, "add"), 0)

    def test_subtract(self):
        self.assertEqual(calculate(7, 2, "subtract"), 5)

    def test_multiply(self):
        self.assertEqual(calculate(7, 2, "multiply"), 14)

    def test_divide(self):
        self.assertEqual(calculate(7, 2, "divide"), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculate(7, 0, "divide")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calculate(7, 2, "modulus")

if __name__ == "__main__":
    unittest.main()
