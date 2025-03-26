MIN_HEIGHT = 50

while True:
    height = input("How tall are you? (Press Enter to quit) ")

    if height == "":
        print("Goodbye!")
        break  # Program band ho jayega

    height = int(height)

    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")
