
from .expense import Expense
from .file_handler import load_expenses, save_expenses


class ExpenseManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.expenses = []
        self.load_data()

    def load_data(self):
        data = load_expenses(self.file_path)
        self.expenses = [Expense.from_dict(item) for item in data]

    def save_data(self):
        data = [expense.to_dict() for expense in self.expenses]
        save_expenses(data, self.file_path)

    def add_expense(self, amount, category, description, date=None):
        expense = Expense(amount, category, description, date)
        self.expenses.append(expense)
        self.save_data()
        return expense

    def get_all_expenses(self):
        return self.expenses

    def search_expenses(self, keyword):
        keyword = keyword.lower()

        return [
            expense for expense in self.expenses
            if keyword in expense.description.lower()
            or keyword in expense.category.lower()
        ]

    def filter_by_category(self, category):
        return [
            expense for expense in self.expenses
            if expense.category.lower() == category.lower()
        ]

    def filter_by_date(self, date):
        return [
            expense for expense in self.expenses
            if expense.date == date
        ]

    def delete_expense(self, index):
        if index < 0 or index >= len(self.expenses):
            return False

        self.expenses.pop(index)
        self.save_data()
        return True

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def clear_all(self):
        self.expenses.clear()
        self.save_data()
