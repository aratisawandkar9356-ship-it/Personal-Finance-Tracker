
import unittest

from finance_tracker.expense import Expense
from finance_tracker.reports import (
    total_expenses,
    category_report,
    monthly_report
)


class TestReports(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            Expense(100, "Food", "Lunch", "2026-11-01"),
            Expense(200, "Travel", "Bus", "2026-11-02"),
            Expense(150, "Food", "Dinner", "2026-12-01")
        ]

    def test_total_expenses(self):
        self.assertEqual(total_expenses(self.expenses), 450)

    def test_category_report(self):
        result = category_report(self.expenses)

        self.assertEqual(result["Food"], 250)
        self.assertEqual(result["Travel"], 200)

    def test_monthly_report(self):
        result = monthly_report(self.expenses)

        self.assertEqual(result["2026-11"], 300)
        self.assertEqual(result["2026-12"], 150)

    def test_empty_expenses(self):
        self.assertEqual(total_expenses([]), 0)
        self.assertEqual(category_report([]), {})
        self.assertEqual(monthly_report([]), {})


if __name__ == "__main__":
    unittest.main()
