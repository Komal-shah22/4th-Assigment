phonebook = {}

while True:
    name = input("Enter a name: ")
    if name == "":
        break  # agar user enter dabaye bina kuch likhe toh stop

    number = input(f"Enter phone number for {name}: ")
    phonebook[name] = number

print("\nPhonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")
