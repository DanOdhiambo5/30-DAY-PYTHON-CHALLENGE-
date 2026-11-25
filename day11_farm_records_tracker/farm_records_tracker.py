# Allows us to work with CSV files
import csv

# Lets us check whether a file exists
import os

# Stores CSV filename
FILE_NAME = "farm_records.csv"


# Creates the CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            # Writes the column headings
            writer.writerow(["Date", "Activity", "Item", "Quantity", "Unit", "Notes"])

        print("Farm records file created successfully!")


# Defines a function to add farm records
def add_record():
    print("\n--- ADD FARM RECORD ---")

    # Collects information from the user
    date = input("Enter date (YYYY-MM-DD): ")
    activity = input("Enter activity (Planting, Harvesting, Feeding, etc.): ")
    item = input("Enter item (Maize, Beans, Fertilizer, etc.): ")

    # Validates quantity
    while True:
        try:
            quantity = float(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than zero.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    unit = input("Enter unit (kg, bags, acres, litres, etc.): ")
    notes = input("Enter additional notes: ")

    # Opens CSV file in append mode
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, activity, item, quantity, unit, notes])

    print("Farm record added successfully!")


# Defines a function to view farm records
def view_records():
    print("\n--- FARM RECORDS ---")

    with open(FILE_NAME, "r", newline="") as file:

        # Reads each CSV row as a dictionary
        reader = csv.DictReader(file)

        # Loops through every saved record
        for record in reader:
            print("----------------------")
            print(f"Date: {record['Date']}")
            print(f"Activity: {record['Activity']}")
            print(f"Item: {record['Item']}")
            print(f"Quantity: {record['Quantity']} {record['Unit']}")
            print(f"Notes: {record['Notes']}")


# Main menu
def main():
    while True:
        print("\n===== FARM RECORDS TRACKER =====")
        print("1. Add farm record")
        print("2. View farm records")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_record()

        elif choice == "2":
            view_records()

        elif choice == "3":
            print("Thank you for using Farm Records Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


# Starts the program
create_file()
main()

    

