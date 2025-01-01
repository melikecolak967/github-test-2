import unittest
from main import calculate  # Burada 'calculate' fonksiyonunu import ediyoruz

class TestCalculate(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculate(7, 2, "add"), 9)

    def test_subtract(self):
        self.assertEqual(calculate(7, 2, "subtract"), 5)

    def test_multiply(self):
        self.assertEqual(calculate(7, 2, "multiply"), 14)

    def test_divide(self):
        self.assertEqual(calculate(7, 2, "divide"), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            calculate(7, 0, "divide")
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_invalid_operation(self):
        with self.assertRaises(ValueError) as context:
            calculate(7, 2, "modulus")
        self.assertEqual(str(context.exception), "Invalid operation")

if __name__ == "__main__":
    unittest.main()
