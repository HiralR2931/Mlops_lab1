import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.calculator import add, subtract, multiply, power, modulo, compound_operation


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 4), -4)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(7, 0), 0)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(9, 3), 0)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError):
            modulo(5, 0)

    def test_compound_operation(self):
        self.assertEqual(compound_operation(2, 3, 4), 20)  # (2 + 3) * 4

    def test_invalid_inputs(self):
        for func in (add, subtract, multiply, power, modulo):
            with self.subTest(func=func.__name__):
                with self.assertRaises(ValueError):
                    func("a", 2)


if __name__ == "__main__":
    unittest.main()
