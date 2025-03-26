MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed:", removed_item)

def main():
    size = int(input("Kitne elements chahiye list mein? "))
    my_list = []
    for i in range(size):
        element = input(f"Element {i+1} likhein: ")
        my_list.append(element)

    print("Original List:", my_list)
    shorten(my_list)
    print("Shortened List:", my_list)

# Run the program
main()
