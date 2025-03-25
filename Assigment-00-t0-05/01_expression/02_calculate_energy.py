C: int = 299792458

def calculate_energy(mass: float) -> float:
    """
    This function calculates energy using Einstein's formula E = m * C^2.
    :param mass: Mass in kilograms
    :return: Energy in joules
    """
    return mass * (C ** 2)

def main():
    while True:
        try:
            mass_in_kg: float = float(input("\nEnter kilos of mass: "))
            if mass_in_kg < 0:
                print("Mass cannot be negative. Please enter a valid value.")
                continue
            
            # Calculate energy
            energy_in_joules: float = calculate_energy(mass_in_kg)

            # Display work to the user
            print("\ne = m * C^2...")
            print(f"m = {mass_in_kg} kg")
            print(f"C = {C} m/s")
            print(f"{energy_in_joules:.2e} joules of energy!")

            # Ask if the user wants to continue
            choice = input("\nDo you want to enter another mass? (yes/no): ").strip().lower()
            if choice != 'yes':
                print("Thank you for using the Mass-Energy Calculator!")
                break

        except ValueError:
            print("Invalid input! Please enter a numerical value.")

# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()
