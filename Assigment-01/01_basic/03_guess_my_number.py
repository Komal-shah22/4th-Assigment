print("\n\t\t\t~~~~~Number Guessing Game~~~~~\n")
import random
allowed_attempt:int = 5
user_attempt:int = 0
while user_attempt < allowed_attempt:
    randon_int = random.randint(1,10)
    user_input = int(input("Enter the number between 1 & 10 :"))
    if(randon_int == user_input):
        print("\t\t\t~~~~~~~~congratulation! you guessed the right number~~~~~~~~\t\t\t")
        break
    else:
        print("you guessed the wrong number! try again")