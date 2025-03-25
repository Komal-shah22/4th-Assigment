def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

print("\n\t\t=========   Simple Addition Tool   ========= ")

while True:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = add_numbers(a, b)
    print("\nThe sum of the given numbers is:", result)

    choice = input("\nDo you want to add more numbers? (yes/no): ").strip().lower()
    
    if choice != "yes":
        print("\n Thank you for using the Addition Tool! Goodbye! ")
        break  


