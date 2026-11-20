# Create an empty list to hold all expenses while the program is running.
expenses = []


# Ask the user for an expense and check that the information is valid.
def add_expense():
    # Get the expense description and category from the user.
    description = input("What did you buy? ").strip()
    category = input("Enter category: ").strip()

    # Make sure the user has entered both a description and a category.
    if not description or not category:
        print("Description and category cannot be empty.")
        return

    # Convert the amount to a number and reject invalid or negative amounts.
    try:
        amount = float(input("Enter amount in KSh: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    # Save the expense as a dictionary inside the expenses list.
    expenses.append({
        "description": description,
        "category": category,
        "amount": amount
    })

    # Confirm that the expense has been saved.
    print("Expense added successfully!")


# Display all expenses that have been added to the list.
def view_expenses():
    # Check whether the list is empty before trying to display expenses.
    if not expenses:
        print("No expenses recorded.")
        return

    # Go through each expense and print its description, category, and amount.
    for expense in expenses:
        print(
            expense["description"],
            "-", expense["category"],
            "- KSh", expense["amount"]
        )


# Add together the amounts of all expenses and display the total.
def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: KSh {total:.2f}")


# Keep showing the menu until the user chooses to exit.
while True:
    # Display the actions the user can choose from.
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Exit")

    # Read the user's menu choice.
    choice = input("Choose an option: ")

    # Run the function that matches the selected menu option.
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        # Say goodbye and stop the menu loop.
        print("Goodbye!")
        break
    else:
        # Tell the user when they enter a menu option that does not exist.
        print("Invalid choice. Try again.")
