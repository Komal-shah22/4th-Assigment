import hashlib

# Password ko hash karne wala function
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Login function
def login(stored_logins, email, password_to_check):
    if email in stored_logins:
        hashed = hash_password(password_to_check)
        if stored_logins[email] == hashed:
            return True
    return False

# Example Stored logins
stored_logins = {
    "komalfareed93@gmail.com": hash_password("hello123"),
    "xyz@yahoo.com": hash_password("mypassword")
}

# Example test
email = input("Enter your email: ")
password = input("Enter your password: ")

if login(stored_logins, email, password):
    print("Login Successful!")
else:
    print("Login Failed!")
