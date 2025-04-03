inventory = {
    "apple": 500,
    "banana": 300,
    "orange": 150,
    "pear": 1000,
    "grape": 50
}

def num_in_stock(fruit):
    return inventory.get(fruit, 0)  

def main():
    fruit = input("Enter a fruit: ").lower()  
    stock = num_in_stock(fruit)  
    if stock > 0:
        print("This fruit is in stock! Here is how many:\n", stock)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
