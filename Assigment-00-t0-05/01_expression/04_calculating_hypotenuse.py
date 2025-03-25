import math

def calculate_hypotenuse(ab: float, ac: float) -> float:
    """
    Calculates the hypotenuse using the Pythagorean theorem.
    :param ab: Length of side AB
    :param ac: Length of side AC
    :return: Length of hypotenuse BC
    """
    return math.sqrt(ab ** 2 + ac ** 2)

def main():
    while True:
        try:
            # Taking input for two perpendicular sides
            ab = float(input("Enter the length of AB: "))
            ac = float(input("Enter the length of AC: "))

            if ab <= 0 or ac <= 0:
                print("Side lengths must be positive numbers.")
                continue
            
            # Calculating the hypotenuse
            bc = calculate_hypotenuse(ab, ac)

            # Displaying the result
            print(f"\nThe length of BC (the hypotenuse) is: {bc:.2f}")

            # Asking user if they want to continue
            choice = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
            if choice != "yes":
                print("Thank you for using the Pythagorean Theorem Calculator!")
                break

        except ValueError:
            print("Invalid input! Please enter numerical values.")

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
