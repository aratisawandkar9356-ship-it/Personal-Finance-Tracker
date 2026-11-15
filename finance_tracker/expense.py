
from datetime import datetime


class Expense:
    def __init__(self, amount, category, description, date=None):
        self.amount = float(amount)
        self.category = category.strip()
        self.description = description.strip()
        self.date = date or datetime.now().strftime("%Y-%m-%d")

        if self.amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        try:
            datetime.strptime(self.date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data.get("date")
        )

    def __str__(self):
        return (
            f"{self.date} | ₹{self.amount:.2f} | "
            f"{self.category} | {self.description}"
        )
