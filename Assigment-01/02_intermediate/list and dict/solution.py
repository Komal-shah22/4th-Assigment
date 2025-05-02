def access_element(my_list, index):
    """Function to access an element at a given index."""
    if index < 0 or index >= len(my_list):
        return "Index out of range."
    return my_list[index]

def modify_element(my_list, index, new_value):
    """Function to modify an element at a given index."""
    if index < 0 or index >= len(my_list):
        return "Index out of range."
    my_list[index] = new_value
    return my_list

def slice_list(my_list, start_index, end_index):
    """Function to slice the list from start_index to end_index."""
    if start_index < 0 or end_index > len(my_list) or start_index >= end_index:
        return "Invalid indices for slicing."
    return my_list[start_index:end_index]

def play_game():
    """Game to practice accessing, modifying, and slicing lists."""
    my_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("\t\t\t\t~~~~~~~~~~~Welcome to the Index Game!~~~~~~~~~~~")
    print("Your list:", my_list)
    
    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            try:
                index = int(input("Enter the index to access: "))
                result = access_element(my_list, index)
                print(f"Element at index {index}: {result}")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the index.")
        
        elif choice == '2':
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                result = modify_element(my_list, index, new_value)
                print(f"Updated list: {result}")
            except ValueError:
                print("Invalid input. Please enter a valid integer for the index.")
        
        elif choice == '3':
            try:
                start_index = int(input("Enter the start index for slicing: "))
                end_index = int(input("Enter the end index for slicing: "))
                result = slice_list(my_list, start_index, end_index)
                print(f"Sliced list: {result}")
            except ValueError:
                print("Invalid input. Please enter valid integers for the indices.")
        
        elif choice == '4':
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    play_game()