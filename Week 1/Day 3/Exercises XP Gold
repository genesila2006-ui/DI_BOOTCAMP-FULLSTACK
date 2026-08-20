# Python
birthdays = {
    "Alice": "1995/04/12",
    "Bob": "1988/11/23",
    "Charlie": "2000/01/05",
    "Dana": "1992/07/19",
    "Eli": "1999/09/30"
}

print("Welcome! Here are the names in our birthday list:")

# 1. Print all names in the dictionary
for name in birthdays.keys():
    print(f"- {name}")

search_name = input("\nEnter a person's name to look up: ").strip()

# 2. Check if person exists and handle missing entries
if search_name in birthdays:
    print(f"{search_name}'s birthday is {birthdays[search_name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {search_name}")
# Exercise 3: Add Your Own Birthday

# Python
birthdays = {
    "Alice": "1995/04/12",
    "Bob": "1988/11/23",
    "Charlie": "2000/01/05",
    "Dana": "1992/07/19",
    "Eli": "1999/09/30"
}

# 1. Prompt user to add a new birthday first
new_name = input("Add a new person's name: ").strip()
new_bday = input("Enter their birthday (YYYY/MM/DD): ").strip()
birthdays[new_name] = new_bday

print("\nUpdated list of people:")
for name in birthdays.keys():
    print(f"- {name}")

# 2. Look up name (works for existing and newly added entries)
search_name = input("\nEnter a person's name to look up: ").strip()

if search_name in birthdays:
    print(f"{search_name}'s birthday is {birthdays[search_name]}.")
else:
    print(f"Sorry, we don’t have the birthday information for {search_name}")
# Exercise 4: Fruit Shop

# Python
# Part 1: Print items and prices in a sentence
items_simple = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

for fruit, price in items_simple.items():
    print(f"A(n) {fruit} costs ${price:.2f}.")

print("-" * 30)

# Part 2: Calculate total cost of everything in stock
items_stock = {
    "banana": {"price": 4, "stock": 10},
    "apple": {"price": 2, "stock": 5},
    "orange": {"price": 1.5, "stock": 24},
    "pear": {"price": 3, "stock": 1}
}

total_stock_value = 0

for fruit, info in items_stock.items():
    item_total = info["price"] * info["stock"]
    total_stock_value += item_total

print(f"Total cost to buy everything in stock: ${total_stock_value:.2f}")