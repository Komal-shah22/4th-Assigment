affirmation = "I am capable of doing anything I put my mind to."

while True:
    user_input = input(f"Please type the following affirmation: {affirmation}\n")
    if user_input == affirmation:
        print("That's right! :)")
        break
    else:
        print("Hmmm That was not the affirmation. Try again.\n")
