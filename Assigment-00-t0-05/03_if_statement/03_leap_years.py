# User se year lena
year = int(input("Koi bhi year likhiye: "))

# Leap year check karna
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    else:
        print("That's a leap year!")
else:
    print("That's not a leap year.")
