
import unittest
import tempfile
import json
from pathlib import Path

from finance_tracker.file_handler import (
    load_expenses,
    save_expenses,
    create_backup,
    restore_backup,
    export_to_csv
)


class TestFileHandler(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp_dir.name)
        self.file_path = self.folder / "expenses.json"
        self.backup_folder = self.folder / "backup"
        self.export_path = self.folder / "exports" / "expenses.csv"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_and_load(self):
        data = [{"amount": 100, "category": "Food"}]
        save_expenses(data, self.file_path)

        result = load_expenses(self.file_path)
        self.assertEqual(result, data)

    def test_load_missing_file(self):
        result = load_expenses(self.file_path)
        self.assertEqual(result, [])

    def test_create_backup(self):
        save_expenses([], self.file_path)
        result = create_backup(self.file_path, self.backup_folder)

        self.assertTrue(result.exists())

    def test_restore_backup(self):
        original = [{"amount": 100, "category": "Food"}]
        save_expenses(original, self.file_path)
        create_backup(self.file_path, self.backup_folder)

        save_expenses([], self.file_path)
        restore_backup(self.backup_folder, self.file_path)

        self.assertEqual(load_expenses(self.file_path), original)

    def test_export_csv(self):
        data = [{
            "date": "2026-11-15",
            "amount": 100,
            "category": "Food",
            "description": "Lunch"
        }]

        result = export_to_csv(data, self.export_path)
        self.assertTrue(result.exists())

    def test_corrupted_json(self):
        self.file_path.write_text("{invalid json", encoding="utf-8")

        with self.assertRaises(ValueError):
            load_expenses(self.file_path)


if __name__ == "__main__":
    unittest.main()
