def calculate_ages():
    Anton = 21
    Beth = Anton + 6
    Chen = Beth + 20
    Drew = Chen + Anton
    Ethan = Chen

    return {"Anton": Anton, "Beth": Beth, "Chen": Chen, "Drew": Drew, "Ethan": Ethan}

ages = calculate_ages()

for name, age in ages.items():
    print(f"{name} is {age}")
