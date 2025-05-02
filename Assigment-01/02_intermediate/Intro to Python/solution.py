MERCURY_CONSTANT: float = 0.376
VENUS_CONSTANT: float = 0.889
MARS_CONSTANT: float = 1.378
JUPITER_CONSTANT: float = 2.360
SATURN_CONSTANT: float = 1.081
URANUS_CONSTANT: float = 0.815
NEPTUNE_CONSTANT: float = 1.140

def calculate_weight():
    while True:
        try:
            earth_weight = float(input("What is your weight on Earth: "))
            break  
        except ValueError:
            print("Weight must be a numeric value. Please try again.")
    
    planet = input("Enter the planet name (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")

    if planet == 'Mercury':
        weight = earth_weight * MERCURY_CONSTANT
    elif planet == 'Venus':
        weight = earth_weight * VENUS_CONSTANT
    elif planet == 'Mars':
        weight = earth_weight * MARS_CONSTANT
    elif planet == 'Jupiter':
        weight = earth_weight * JUPITER_CONSTANT
    elif planet == 'Saturn':
        weight = earth_weight * SATURN_CONSTANT
    elif planet == 'Uranus':
        weight = earth_weight * URANUS_CONSTANT
    elif planet == 'Neptune':
        weight = earth_weight * NEPTUNE_CONSTANT
    else:
        print("Invalid planet name entered.")
        return

    print(f"Your weight on {planet} is: {weight:.2f}")

calculate_weight()