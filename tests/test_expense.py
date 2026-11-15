
import unittest

from finance_tracker.expense import Expense


class TestExpense(unittest.TestCase):

    def test_create_expense(self):
        expense = Expense(100, "Food", "Lunch", "2026-11-15")
        self.assertEqual(expense.amount, 100)
        self.assertEqual(expense.category, "Food")

    def test_expense_to_dict(self):
        expense = Expense(200, "Travel", "Bus")
        data = expense.to_dict()

        self.assertEqual(data["amount"], 200)
        self.assertEqual(data["category"], "Travel")

    def test_expense_from_dict(self):
        data = {
            "amount": 300,
            "category": "Shopping",
            "description": "Shoes",
            "date": "2026-11-15"
        }

        expense = Expense.from_dict(data)
        self.assertEqual(expense.amount, 300)

    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            Expense(-100, "Food", "Lunch")

    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            Expense(0, "Food", "Lunch")

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            Expense(100, "Food", "Lunch", "15-11-2026")


if __name__ == "__main__":
    unittest.main()
