def divide_numbers():
    """
    Asks the user for two integers, prints the quotient and remainder, and handles errors.
    """
    print("\n\t\t\t======= Welcome to the Division Calculator! ========\n")
    print("This program divides two numbers and gives the quotient and remainder.\n")

    while True:
        try:
            # Taking user input
            num1 = int(input("Please enter an integer to be divided: "))
            num2 = int(input("Please enter an integer to divide by: "))

            # Handling division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed. Please enter a valid divisor.\n")
                continue
            
            # Performing division
            quotient = num1 // num2  # Integer division
            remainder = num1 % num2  # Modulus operator to find remainder

            # Displaying result
            print(f"\nThe result of this division is {quotient} with a remainder of {remainder}\n")

            # Asking user if they want to continue
            choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if choice != "yes":
                print("\nThank you for using the Division Calculator! Have a great day!")
                break

        except ValueError:
            print("Invalid input! Please enter valid integer values.\n")

# Calling the function
divide_numbers()
