def get_last_element(lst):
    print("Last element is:", lst[-1])

# Main Program
size = int(input("Kitne elements chahiye list mein? "))

my_list = []
for i in range(size):
    element = input(f"Element {i+1} likhein: ")
    my_list.append(element)

print("Aapki list:", my_list)

# Call function
get_last_element(my_list)
