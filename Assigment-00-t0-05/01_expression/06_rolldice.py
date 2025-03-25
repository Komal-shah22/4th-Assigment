import random

def roll_dice():
    """
    Simulates rolling two dice and prints the results.
    """
    print("Welcome to the Dice Rolling Simulator!\n")

    while True:
        die1 = random.randint(1, 6) 
        die2 = random.randint(1, 6) 
        total = die1 + die2 

        print(f"You rolled: {die1} and {die2}")
        print(f"Total: {total}\n")

        # Asking user if they want to roll again
        choice = input("Roll again? (yes/no): ").strip().lower()
        if choice != "yes":
            print("\nThank you for playing! Have a great day!")
            break

# Calling the function
roll_dice()
