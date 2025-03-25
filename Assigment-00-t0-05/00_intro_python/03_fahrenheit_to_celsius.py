def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5.0 / 9.0

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print(f"\nTemperature: {fahrenheit:.1f}F = {celsius:.2f}C")
