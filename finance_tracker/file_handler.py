
import json
import csv
import shutil
from pathlib import Path


def load_expenses(file_path):
    path = Path(file_path)

    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("[]", encoding="utf-8")
        return []

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("Invalid expenses file format.")

        return data

    except json.JSONDecodeError:
        raise ValueError("Expenses JSON file is corrupted.")


def save_expenses(expenses, file_path):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4, ensure_ascii=False)


def create_backup(file_path, backup_folder):
    source = Path(file_path)
    backup_dir = Path(backup_folder)

    if not source.exists():
        return None

    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / "expenses_backup.json"

    shutil.copy2(source, backup_path)
    return backup_path


def restore_backup(backup_folder, file_path):
    backup_path = Path(backup_folder) / "expenses_backup.json"
    destination = Path(file_path)

    if not backup_path.exists():
        raise FileNotFoundError("Backup file not found.")

    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(backup_path, destination)


def export_to_csv(expenses, file_path):
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    fields = ["date", "amount", "category", "description"]

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()

        for expense in expenses:
            writer.writerow({
                "date": expense.get("date", ""),
                "amount": expense.get("amount", 0),
                "category": expense.get("category", ""),
                "description": expense.get("description", "")
            })

    return path
