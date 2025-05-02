
import random

PROMPT: str = "What do you want? (Type 'joke' to hear a joke): "

JOKES: list = [
    '''Teacher: "Why are you late?"
    Student: "Because I started walking before I left!" 😄''',
    
    '''Why don't skeletons fight each other? 
    They don't have the guts! 😄''',
    
    '''Why don't eggs tell jokes? 
    Because they'd crack each other up! 🥚😄''',
    
    '''Why did the computer go to the doctor? 
    It had a virus! 🦠💻''',
    
    '''What did one ocean say to the other ocean? 
    Nothing, they just waved! 🌊👋'''
]

def joke_bot():
    user_input = input(PROMPT).strip()  
    if not user_input:  
        print("You didn't enter anything. Please type 'joke' if you want to hear a joke.")
        return
    
    if user_input.lower() == "joke":
  
        joke = random.choice(JOKES)
        print(joke)
    else:
        print("Sorry, I only tell jokes.")

joke_bot()