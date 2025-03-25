
def calculate_perimeter():
    print("\n\t\t========= Triangle Perimeter Calculator =========")

    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    perimeter = side1 + side2 + side3

    print(f"\nThe perimeter of the triangle is {perimeter}")

calculate_perimeter()
