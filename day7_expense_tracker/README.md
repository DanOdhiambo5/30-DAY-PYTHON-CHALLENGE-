# Personal Expense Tracker 💰

A simple command-line expense tracker built with Python as part of my 30-Day Python Challenge (Day 7).

## Features

- Add an expense with a description, category, and amount.
- View all recorded expenses.
- Calculate total spending.
- View spending totals grouped by category.
- Validate user input:
  - Description and category cannot be empty.
  - Expense amounts must be valid numbers greater than zero.
  - Menu choices must be between 1 and 5.

## Concepts Practised

- Variables and user input
- Lists and dictionaries
- Loops and conditional statements
- Functions
- Exception handling with `try` and `except`
- Working with dictionary data and calculating totals

## Requirements

- Python 3
- No external packages are required.

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/DanOdhiambo5/30-DAY-PYTHON-CHALLENGE-.git
   ```

2. Open the project folder:

   ```bash
   cd 30-DAY-PYTHON-CHALLENGE-/day7_expense_tracker
   ```

3. Run the program:

   ```bash
   python expense_tracker.py
   ```

## How It Works

The program stores expenses in a list. Each expense is a dictionary containing its description, category, and amount. A menu lets the user add expenses or view spending summaries.

**Note:** This beginner version stores data in memory only. Expenses are cleared when the program exits. Persistent file storage can be added in a future improvement.

## Author

Dan Odhiambo — [GitHub](https://github.com/DanOdhiambo5)
