# 📋 Expense Tracker CLI

A simple Python command-line tool to log and categorize personal expenses, generate monthly summaries, and export data to CSV — built with `argparse`, `pandas`, and file I/O.

---

## 🚀 Features

- Add and categorize expenses
- View monthly summaries
- List all expenses with total spent
- Export to CSV
- Lightweight: uses a local CSV file for storage

---

## 🛠️ Requirements

- Python 3.7 or higher
- pandas

Install pandas with:

```bash
pip install pandas
```

---

## 💻 How to Use

```bash
# Add an expense
python3 expense_tracker.py add 15.99 food "Lunch at cafe"

# View summary for current month
python3 expense_tracker.py summary

# View summary for a specific month (YYYY-MM)
python3 expense_tracker.py summary --month 2025-06

# List all expenses in a table and show total spent
python3 expense_tracker.py list

# Export all expenses to a custom CSV file
python3 expense_tracker.py export --output my_expenses.csv
```

---

## 📁 Data Format

Expenses are saved in `expenses.csv` with the following columns:

- `date`: auto-filled (YYYY-MM-DD)
- `amount`: float
- `category`: string (e.g., food, transport)
- `description`: string

Example row:

```
2025-06-08,15.99,food,Lunch at cafe
```

---

## 📝 Sample Output

```bash
📄 All logged expenses:

      date  amount category       description
2025-06-08   15.99     food    Lunch at cafe

📟 Total Spent: $15.99
```

---

## 📌 Notes

- Your data is saved locally in `expenses.csv`
- Easily extensible with filters, category totals, or charts
- Great starting point for a budget app or TUI

---