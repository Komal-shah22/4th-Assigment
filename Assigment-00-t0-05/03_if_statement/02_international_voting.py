def check_voting_rights():
    age = int(input("Aapki age kya hai? "))

    if age >= 18:
        print("Aap Pakistan mein vote kar sakte hain (Voting age: 18).")
    else:
        print("Aap Pakistan mein vote nahi kar sakte (Voting age: 18).")

    if age >= 21:
        print("Aap USA mein vote kar sakte hain (Voting age: 21).")
    else:
        print("Aap USA mein vote nahi kar sakte (Voting age: 21).")

    if age >= 30:
        print("Aap Japan mein vote kar sakte hain (Voting age: 30).")
    else:
        print("Aap Japan mein vote nahi kar sakte (Voting age: 30).")

# Program run karein
check_voting_rights()
