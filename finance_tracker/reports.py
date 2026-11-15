
from collections import defaultdict


def total_expenses(expenses):
    return sum(item.amount for item in expenses)


def category_report(expenses):
    result = defaultdict(float)

    for item in expenses:
        result[item.category] += item.amount

    return dict(result)


def monthly_report(expenses):
    result = defaultdict(float)

    for item in expenses:
        month = item.date[:7]
        result[month] += item.amount

    return dict(result)


def show_report(expenses):
    if not expenses:
        print("\nNo expenses available for report.")
        return

    print("\n========== EXPENSE REPORT ==========")
    print(f"Total Expenses: ₹{total_expenses(expenses):.2f}")
    print(f"Number of Transactions: {len(expenses)}")

    print("\nCategory-wise Expenses:")
    for category, amount in category_report(expenses).items():
        print(f"{category}: ₹{amount:.2f}")

    print("\nMonthly Expenses:")
    for month, amount in monthly_report(expenses).items():
        print(f"{month}: ₹{amount:.2f}")

    print("====================================")


def create_chart(expenses, output_path):
    if not expenses:
        print("No expenses available to create chart.")
        return

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        categories = category_report(expenses)

        plt.figure(figsize=(9, 5))
        plt.bar(categories.keys(), categories.values())
        plt.title("Category-wise Expense Report")
        plt.xlabel("Category")
        plt.ylabel("Amount (₹)")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.savefig(output_path)
        plt.close()

        print(f"Chart saved successfully: {output_path}")

    except ImportError:
        print("Matplotlib is not installed. Install it using pip.")
