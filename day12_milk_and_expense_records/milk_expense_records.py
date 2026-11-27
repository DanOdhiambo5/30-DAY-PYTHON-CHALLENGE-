# WEEK 2 - DAY 12: MILK PRODUCTION AND EXPENSE RECORDS

# BLOCK 1: Create empty lists to store milk and expense records
milk_records = []
expense_records = []


# BLOCK 2: Collect multiple milk production records
while True:
    print("\n--- MILK PRODUCTION RECORD ---")

    date = input("Enter date: ")
    morning = float(input("Enter morning milk production (litres): "))
    evening = float(input("Enter evening milk production (litres): "))

    # Store the daily milk information in a dictionary
    milk_record = {
        "date": date,
        "morning": morning,
        "evening": evening
    }

    # Add the dictionary to the milk records list
    milk_records.append(milk_record)

    # Ask whether the farmer wants to add another record
    another = input("Add another milk record? (yes/no): ").lower()

    if another != "yes":
        break


# BLOCK 3: Collect multiple farm expense records
while True:
    print("\n--- FARM EXPENSE RECORD ---")

    date = input("Enter expense date: ")
    expense = input("Enter expense description: ")
    amount = float(input("Enter expense amount (KSh): "))

    # Store expense information in a dictionary
    expense_record = {
        "date": date,
        "expense": expense,
        "amount": amount
    }

    # Add the expense dictionary to the expense records list
    expense_records.append(expense_record)

    # Ask whether the farmer wants to add another expense
    another = input("Add another expense? (yes/no): ").lower()

    if another != "yes":
        break


# BLOCK 4: Calculate total milk production across all records
total_milk = 0

for record in milk_records:
    total_milk += record["morning"] + record["evening"]


# BLOCK 5: Calculate total expenses across all records
total_expenses = 0

for record in expense_records:
    total_expenses += record["amount"]


# BLOCK 6: Display individual milk production records
print("\n========== MILK PRODUCTION REPORT ==========")

for record in milk_records:
    daily_total = record["morning"] + record["evening"]

    print(f"Date: {record['date']}")
    print(f"Morning: {record['morning']} litres")
    print(f"Evening: {record['evening']} litres")
    print(f"Daily Total: {daily_total} litres")
    print("----------------------------------")


# BLOCK 7: Display individual farm expense records
print("\n========== FARM EXPENSE REPORT ==========")

for record in expense_records:
    print(f"Date: {record['date']}")
    print(f"Expense: {record['expense']}")
    print(f"Amount: KSh {record['amount']:.2f}")
    print("----------------------------------")


# BLOCK 8: Display the final farm summary
print("\n========== FARM SUMMARY ==========")

print(f"Total Milk Produced: {total_milk:.2f} litres")
print(f"Total Farm Expenses: KSh {total_expenses:.2f}")


# BLOCK 9: Confirm successful program completion
print("\nDay 12 program completed successfully!")
