# Keep the program running until the user chooses to exit.
while True:

    # Ask the user to enter a number.
    number = int(input("\nEnter a number: "))

    # Display the multiplication table heading.
    print(f"\nMultiplication table for {number}")

    # Repeat the calculation from 1 to 10.
    for i in range(1, 11):

        # Multiply the user's number by the current loop number.
        result = number * i

        # Display the multiplication result.
        print(f"{number} x {i} = {result}")

    # Ask the user whether they want another table.
    choice = input("\nWould you like another table? (yes/no): ").lower()

    # Stop the program if the user chooses no.
    if choice == "no":
        print("Thank you for using the multiplication table generator!")
        break

    # Continue if the user chooses yes.
    elif choice == "yes":
        print("Let's generate another table!")

    # Handle an invalid response.
    else:
        print("Invalid choice. Please enter yes or no.")
