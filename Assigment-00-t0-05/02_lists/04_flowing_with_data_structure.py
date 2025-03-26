def add_three_copies(my_list, data):
    for _ in range(3):
        my_list.append(data)

# Main Program
message = input("Enter a message to copy: ")

# Empty list
messages = []

print("List before:", messages)

# Call the function
add_three_copies(messages, message)

print("List after:", messages)
