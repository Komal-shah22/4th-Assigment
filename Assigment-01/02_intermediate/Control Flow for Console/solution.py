
import random

NUM_ROUNDS = 5 

def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    
    score = 0 
    
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        while True:
            guess = input("Do you think your number is higher or lower than the computer's? (Enter 'higher' or 'lower'): ").strip().lower()
            if guess in ["higher", "lower"]:
                break
            print("Invalid input. Please enter 'higher' or 'lower'.")
        
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            score += 1
            print(f"\n=====You were right! The computer's number was {computer_number}.=====")
        else:
            print(f"\nAww, that's incorrect. The computer's number was {computer_number}.")
        
        print(f"\n\t\t\t~~~~~~~~~~~Your score is now {score}~~~~~~~~\n")
    
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!\n")
    else:
        print("\n\n\t\t\t~~~~~~Better luck next time!~~~~~~~~~")
high_low_game()