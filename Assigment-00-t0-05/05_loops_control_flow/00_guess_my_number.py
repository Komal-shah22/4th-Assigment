import random

def guess_my_number():
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        guess = int(input("Enter a guess: "))
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break

guess_my_number()
