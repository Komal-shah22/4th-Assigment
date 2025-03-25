def print_square()->int :
    print("\n\t\t========= Square Calculator =========\n")
    num = int(input("Type a number to see its square: "))
    square = num * num
    print(f"\n{num} squared is {square}")
    return square

print_square()
