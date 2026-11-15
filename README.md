
# Personal Finance Tracker

## Project Description
Personal Finance Tracker is a Python-based application that helps users manage and track their daily expenses.

Users can add, view, search, filter and delete expenses. The application stores expense information in JSON format and supports CSV export, backup, restore and expense reports.

## Features
- Add and manage expenses
- View all expenses
- Search expenses by category or description
- Filter expenses by category and date
- Delete expenses
- Calculate total expenses
- Generate category-wise and monthly reports
- Export expenses to CSV
- Create and restore JSON backups
- Generate expense charts

## Technologies Used
- Python
- JSON
- CSV
- Matplotlib
- Unittest

## Project Structure
```text
week4-finance-tracker/
    finance_tracker/
    data/
    tests/
    requirements.txt
    README.md
    .gitignore
    run.py
```

## Installation

1. Install Python.
2. Open the project folder in VS Code.
3. Install required library:

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python run.py
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

## Data Storage
Expense details are stored in `data/expenses.json`.

CSV exports are saved in `data/exports/`, and backup files are saved in `data/backup/`.

## Conclusion
The Personal Finance Tracker provides a simple way to manage daily expenses, generate reports and maintain financial records using Python file handling and object-oriented programming.
