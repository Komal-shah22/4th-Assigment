
def double_it():
    try:
        user_input = int(input("Enter a number (greater than 100): "))
        
        if user_input <= 100:
            print("Starting the process to double the number until it exceeds 100:")
            while user_input <= 100:
                user_input *= 2
                print(user_input, end=" ") 
            print("\nDone! Your number has exceeded 100.")
        else:
            print("The number you entered is already greater than 100. No doubling needed.")
    
    except ValueError:
        print("Please enter a valid integer.")

double_it()