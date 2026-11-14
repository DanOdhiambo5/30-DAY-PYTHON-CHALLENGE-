# Store each expense as a dictionary inside a list.
expenses = []


def add_expense():
    description = input("What did you buy? ").strip()
    category = input("Enter category: ").strip()

    if not description or not category:
        print("Description and category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount in KSh: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    expenses.append({
        "description": description,
        "category": category,
        "amount": amount
    })

    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    for expense in expenses:
        print(
            expense["description"],
            "-", expense["category"],
            "- KSh", expense["amount"]
        )


def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: KSh {total:.2f}")


while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
