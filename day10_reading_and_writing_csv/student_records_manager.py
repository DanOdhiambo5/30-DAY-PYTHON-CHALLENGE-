# Import the CSV module to read and write CSV files
import csv

# Import os to check whether a file already exists
import os


# Define the name of the CSV file that stores student records
FILE_NAME = "student_records.csv"


# Create the CSV file if it does not already exist
def create_file():

    # Check whether the student records file exists
    if not os.path.exists(FILE_NAME):

        # Open the file in write mode to create it
        with open(FILE_NAME, "w", newline="") as file:

            # Define the column headings
            writer = csv.DictWriter(
                file,
                fieldnames=["name", "age", "course"]
            )

            # Write the column headings into the CSV file
            writer.writeheader()


# Function for adding a new student
def add_student():

    print("\n--- Add Student ---")

    # Collect student information from the user
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    # Store the collected information in a dictionary
    student = {
        "name": name,
        "age": age,
        "course": course
    }

    # Open the CSV file in append mode so existing records are preserved
    with open(FILE_NAME, "a", newline="") as file:

        # Create a CSV dictionary writer
        writer = csv.DictWriter(
            file,
            fieldnames=["name", "age", "course"]
        )

        # Add the new student's information to the CSV file
        writer.writerow(student)

    # Confirm that the student was saved successfully
    print("\nStudent added successfully!")


# Function for displaying all saved student records
def view_students():

    print("\n--- Student Records ---")

    # Open the CSV file in read mode
    with open(FILE_NAME, "r", newline="") as file:

        # Read CSV records as dictionaries
        reader = csv.DictReader(file)

        # Convert the records into a list
        students = list(reader)

        # Check whether the CSV file contains any student records
        if not students:
            print("No student records found.")
            return

        # Loop through each student and display their information
        for student in students:
            print(
                f"Name: {student['name']} | "
                f"Age: {student['age']} | "
                f"Course: {student['course']}"
            )


# Main function controls the application
def main():

    # Make sure the CSV file exists before starting
    create_file()

    # Keep displaying the menu until the user chooses to exit
    while True:

        # Display the application menu
        print("\n===== STUDENT RECORDS MANAGER =====")
        print("1. Add student")
        print("2. View students")
        print("3. Exit")

        # Ask the user to select an option
        choice = input("\nEnter your choice: ")

        # Run the function for adding a student
        if choice == "1":
            add_student()

        # Run the function for viewing student records
        elif choice == "2":
            view_students()

        # Exit the application
        elif choice == "3":
            print("Thank you for using Student Records Manager!")
            break

        # Handle invalid menu selections
        else:
            print("Invalid choice. Please try again.")


# Check whether this file is being run directly
if __name__ == "__main__":

    # Start the application
    main()
