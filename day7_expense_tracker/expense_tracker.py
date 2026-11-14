"""A simple command-line expense tracker.

Users can add expenses, view their records, and review spending totals.
All data is stored in memory and will reset when the program closes.
"""


def get_non_empty_text(prompt):
    """Keep asking until the user enters non-empty text."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def get_positive_amount():
    """Get a valid expense amount greater than zero."""
    while True:
        amount_text = input("Enter amount in KSh: ").strip()

        try:
            amount = float(amount_text)
            if amount > 0:
                return amount
            print("Amount must be greater than zero.")
        except ValueError:
            print("Please enter a valid number, for example 250 or 99.50.")


def add_expense(expenses):
    """Collect expense details and add them to the expenses list."""
    print("\n--- Add an Expense ---")
    description = get_non_empty_text("What did you spend on? ")
    category = get_non_empty_text("Category (e.g. Food, Transport): ").title()
    amount = get_positive_amount()

    # Each expense is stored as a dictionary inside the expenses list.
    expense = {
        "description": description,
        "category": category,
        "amount": amount,
    }
    expenses.append(expense)

    print(f"Expense added: {description} - KSh {amount:,.2f}")


def view_expenses(expenses):
    """Display every expense recorded so far."""
    print("\n--- All Expenses ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number}. {expense['description']} | "
            f"{expense['category']} | KSh {expense['amount']:,.2f}"
        )


def show_total(expenses):
    """Calculate and display the total amount spent."""
    total = sum(expense["amount"] for expense in expenses)
    print(f"\nTotal spending: KSh {total:,.2f}")


def show_category_totals(expenses):
    """Group expenses by category and display each category total."""
    print("\n--- Spending by Category ---")

    if not expenses:
        print("No expenses recorded yet.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        # Add to the category total, or start it at zero.
        category_totals[category] = category_totals.get(category, 0) + amount

    for category, total in category_totals.items():
        print(f"{category}: KSh {total:,.2f}")


def main():
    """Run the expense tracker menu."""
    expenses = []

    while True:
        print("\n====== PERSONAL EXPENSE TRACKER ======")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View total spending")
        print("4. View spending by category")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            show_category_totals(expenses)
        elif choice == "5":
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
