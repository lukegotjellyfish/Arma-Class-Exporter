import sys
import unittest
from decimal import Decimal

sys.path.append('..')
from ArmaClassExporter import eval_param_value as epv


class TestEvalExpr(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(epv.eval_expr("2 + 3"), 5)
        self.assertEqual(epv.eval_expr("10 - 5"), 5)
        self.assertEqual(epv.eval_expr("4 * 3"), 12)
        self.assertEqual(epv.eval_expr("8 / 2"), 4.0)

    def test_operator_precedence(self):
        self.assertEqual(epv.eval_expr("2 + 3 * 4"), 14)
        self.assertEqual(epv.eval_expr("(2 + 3) * 4"), 20)
        self.assertEqual(epv.eval_expr("2 ** 3 + 1"), 9)

    def test_unary_operations(self):
        self.assertEqual(epv.eval_expr("-5"), -5)
        self.assertEqual(epv.eval_expr("5 + (-3)"), 2)
        self.assertEqual(epv.eval_expr("-2 ** 2"), -4)

    def test_power_operations(self):
        self.assertEqual(epv.eval_expr("2 ** 3"), 8)
        self.assertEqual(epv.eval_expr("4 ** 0.5"), 2.0)

    def test_division(self):
        self.assertEqual(epv.eval_expr("10 / 4"), 2.5)
        self.assertEqual(epv.eval_expr("5 / 2"), 2.5)

    def test_errors(self):
        with self.assertRaises(ValueError):
            epv.eval_expr("2 +")
        with self.assertRaises(ValueError):
            epv.eval_expr("2 / 0")
        with self.assertRaises(ValueError):
            epv.eval_expr("unsupported + 1")

class TestDecimalize(unittest.TestCase):
    def test_decimalize(self):
        self.assertEqual(epv.decimalize("2.5 * 2"), Decimal("5.0"))
        self.assertEqual(epv.decimalize("0.5"), Decimal("0.5"))
        self.assertEqual(epv.decimalize("0.5 + 0.5"), Decimal("1.0"))

if __name__ == '__main__':
    unittest.main()