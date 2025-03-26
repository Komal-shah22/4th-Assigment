# Fruits ke naam aur unki prices
fruit_prices = {
    "apple": 10.5,
    "durian": 25.0,
    "jackfruit": 15.0,
    "kiwi": 8.0,
    "rambutan": 12.0,
    "mango": 9.0
}

total_cost = 0

# User se har fruit ke quantity poochhna
for fruit, price in fruit_prices.items():
    quantity = int(input(f"How many ({fruit}) do you want?: "))
    total_cost += quantity * price

print(f"\nYour total is ${total_cost}")
