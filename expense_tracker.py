import argparse
import pandas as pd
from datetime import datetime
import os

CSV_FILE = 'expenses.csv'
COLUMNS = ['date', 'amount', 'category', 'description']

#initialization
if not os.path.exists(CSV_FILE):
    pd.DataFrame(columns=COLUMNS).to_csv(CSV_FILE, index=False)

def add_expense(args):
    new_expense = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'amount': float(args.amount),
        'category': args.category,
        'description': args.description
    }
    df = pd.read_csv(CSV_FILE)
    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)
    print("✅ Expense added successfully.")

def show_summary(args):
    df = pd.read_csv(CSV_FILE)
    if df.empty:
        print("⚠️ No expenses logged yet.")
        return

    df['date'] = pd.to_datetime(df['date'])
    month = args.month or datetime.now().strftime('%Y-%m')
    df_month = df[df['date'].dt.strftime('%Y-%m') == month]

    if df_month.empty:
        print(f"⚠️ No expenses found for {month}.")
        return

    summary = df_month.groupby('category')['amount'].sum().reset_index()
    print(f"📊 Summary for {month}:")
    print(summary.to_string(index=False))

def export_data(args):
    df = pd.read_csv(CSV_FILE)
    export_path = args.output or 'expenses_export.csv'
    df.to_csv(export_path, index=False)
    print(f"📤 Data exported to {export_path}")

def list_expenses(args):
    df = pd.read_csv(CSV_FILE)
    if df.empty:
        print("⚠️ No expenses found.")
    else:
        print("📄 All logged expenses:\n")
        print(df.to_string(index=False))
        total = df['amount'].sum()
        print(f"\n🧾 Total Spent: ${total:.2f}")

def main():
    parser = argparse.ArgumentParser(description='Expense Tracker CLI')
    subparsers = parser.add_subparsers(title='Commands')

    #adding expenses
    parser_add = subparsers.add_parser('add', help='Add a new expense')
    parser_add.add_argument('amount', type=float, help='Amount spent')
    parser_add.add_argument('category', type=str, help='Expense category')
    parser_add.add_argument('description', type=str, help='Expense description')
    parser_add.set_defaults(func=add_expense)

    #summary
    parser_summary = subparsers.add_parser('summary', help='Show monthly summary')
    parser_summary.add_argument('--month', type=str, help='Month in YYYY-MM format (default: current month)')
    parser_summary.set_defaults(func=show_summary)

    #export CSV
    parser_export = subparsers.add_parser('export', help='Export all data to CSV')
    parser_export.add_argument('--output', type=str, help='Output CSV filename')
    parser_export.set_defaults(func=export_data)

    # List all expenses as table
    parser_list = subparsers.add_parser('list', help='Show all expenses as a table')
    parser_list.set_defaults(func=list_expenses)


    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
