import random

def roll_dice():
    print("\n\t\t========= Rolling Dice =========\n")
    
    for i in range(1, 4):
        die1 = random.randint(1, 6) 
        die2 = random.randint(1, 6)

        print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")

roll_dice()

