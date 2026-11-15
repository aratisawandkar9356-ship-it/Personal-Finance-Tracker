
from pathlib import Path

from .expense_manager import ExpenseManager
from .file_handler import (
    create_backup,
    export_to_csv,
    restore_backup
)
from .reports import show_report, create_chart
from .utils import (
    get_valid_amount,
    get_valid_text,
    get_valid_date,
    print_expenses
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_ROOT / "data"
EXPENSE_FILE = DATA_FOLDER / "expenses.json"
BACKUP_FOLDER = DATA_FOLDER / "backup"
EXPORT_FOLDER = DATA_FOLDER / "exports"

manager = ExpenseManager(EXPENSE_FILE)


def add_expense():
    print("\n--- Add New Expense ---")

    amount = get_valid_amount()
    category = get_valid_text("Enter category: ")
    description = get_valid_text("Enter description: ")
    date = get_valid_date()

    try:
        manager.add_expense(amount, category, description, date)
        print("Expense added successfully!")

    except ValueError as error:
        print("Error:", error)


def search_expense():
    keyword = get_valid_text("Enter category or description to search: ")
    results = manager.search_expenses(keyword)
    print_expenses(results)


def filter_expense():
    print("\n1. Filter by Category")
    print("2. Filter by Date")

    choice = input("Enter choice: ")

    if choice == "1":
        category = get_valid_text("Enter category: ")
        results = manager.filter_by_category(category)
        print_expenses(results)

    elif choice == "2":
        date = get_valid_date()
        results = manager.filter_by_date(date)
        print_expenses(results)

    else:
        print("Invalid choice.")


def delete_expense():
    print_expenses(manager.get_all_expenses())

    if not manager.expenses:
        return

    try:
        number = int(input("Enter expense number to delete: "))
        success = manager.delete_expense(number - 1)

        if success:
            print("Expense deleted successfully!")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


def backup_data():
    result = create_backup(EXPENSE_FILE, BACKUP_FOLDER)

    if result:
        print("Backup created:", result)
    else:
        print("No expense file available for backup.")


def export_data():
    file_path = EXPORT_FOLDER / "expenses.csv"
    export_to_csv(
        [item.to_dict() for item in manager.expenses],
        file_path
    )
    print("CSV exported successfully:", file_path)


def restore_data():
    try:
        restore_backup(BACKUP_FOLDER, EXPENSE_FILE)
        manager.load_data()
        print("Backup restored successfully!")

    except FileNotFoundError as error:
        print(error)


def main():
    while True:
        print("\n========== PERSONAL FINANCE TRACKER ==========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Filter Expenses")
        print("5. Delete Expense")
        print("6. View Reports")
        print("7. Export Expenses to CSV")
        print("8. Create Backup")
        print("9. Restore Backup")
        print("10. Create Expense Chart")
        print("11. Exit")
        print("==============================================")

        choice = input("Enter your choice (1-11): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            print_expenses(manager.get_all_expenses())

        elif choice == "3":
            search_expense()

        elif choice == "4":
            filter_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            show_report(manager.get_all_expenses())

        elif choice == "7":
            export_data()

        elif choice == "8":
            backup_data()

        elif choice == "9":
            restore_data()

        elif choice == "10":
            chart_path = EXPORT_FOLDER / "expense_chart.png"
            create_chart(manager.get_all_expenses(), chart_path)

        elif choice == "11":
            print("Thank you for using Personal Finance Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
