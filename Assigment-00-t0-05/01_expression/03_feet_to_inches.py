def feet_to_inches(feet: float) -> float:
    """
    Converts feet to inches.
    :param feet: Length in feet
    :return: Equivalent length in inches
    """
    return feet * 12  # 1 foot = 12 inches

def main():
    while True:
        try:
            feet = float(input("\nEnter length in feet: "))
            if feet < 0:
                print("Length cannot be negative. Please enter a valid value.")
                continue
            
            inches = feet_to_inches(feet)

            # Display the result
            unit = "foot" if feet == 1 else "feet"
            print(f"{feet} {unit} is equal to {inches} inches.")

            # Ask if the user wants to continue
            choice = input("\nDo you want to convert another value? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("Thank you for using the Feet to Inches Converter!")
                break

        except ValueError:
            print("Invalid input! Please enter a numerical value.")

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
