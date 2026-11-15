
from datetime import datetime


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount (₹): "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return amount

        except ValueError:
            print("Please enter a valid number.")


def get_valid_text(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_valid_date():
    while True:
        date = input(
            "Enter date (YYYY-MM-DD) or press Enter for today: "
        ).strip()

        if not date:
            return datetime.now().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


def print_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "-" * 75)
    print(f"{'No.':<5}{'Date':<15}{'Amount':<15}{'Category':<18}Description")
    print("-" * 75)

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index:<5}{expense.date:<15}"
            f"₹{expense.amount:<14.2f}"
            f"{expense.category:<18}{expense.description}"
        )

    print("-" * 75)
