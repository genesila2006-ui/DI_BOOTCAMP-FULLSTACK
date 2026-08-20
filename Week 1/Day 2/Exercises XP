# Exercise 1: Favorite Numbers

# Python
# Create initial set
my_fav_numbers = {3, 7, 11}

# Add two new numbers
my_fav_numbers.add(21)
my_fav_numbers.add(42)

# Remove the last number added (42)
my_fav_numbers.remove(42)

# Friend's favorite numbers
friend_fav_numbers = {5, 7, 13}

# Combine sets using union
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)

print("Our favorite numbers:", our_fav_numbers)
# Exercise 2: Tuple

# Python
my_tuple = (1, 2, 3)

# Attempting to modify or add elements directly to a tuple will raise a TypeError:
# my_tuple[0] = 5  # TypeError: 'tuple' object does not support item assignment
# my_tuple.append(4)  # AttributeError: 'tuple' object has no attribute 'append'

# Explanation:
# Tuples are immutable, meaning their structure and element references cannot be changed once created.
# To "add" elements, you must create a new tuple by concatenating:
new_tuple = my_tuple + (4, 5)
print("New tuple created via concatenation:", new_tuple)
# Exercise 3: List Manipulation

# Python
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# Remove "Banana" and "Blueberries"
basket.remove("Banana")
basket.remove("Blueberries")

# Add "Kiwi" to the end and "Apples" to the beginning
basket.append("Kiwi")
basket.insert(0, "Apples")

# Count occurrences of "Apples"
apples_count = basket.count("Apples")
print(f"'Apples' count: {apples_count}")

# Empty the list
basket.clear()

# Print final state
print("Final basket state:", basket)
# Exercise 4: Floats

# Recap: An integer is a whole number without decimals (e.g., 2), while a float represents numbers with fractional parts/decimal points (e.g., 2.5).

# Python
# Generating sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 using a loop
sequence = []
x = 1.5

while x <= 5.0:
    # Convert whole numbers to integers, keep others as floats
    sequence.append(int(x) if x.is_integer() else x)
    x += 0.5

print(sequence)
# Exercise 5: For Loop

# Python
# Print numbers from 1 to 20, inclusive
print("Numbers 1 to 20:")
for num in range(1, 21):
    print(num, end=" ")
print("\n")

# Print numbers from 1 to 20 where the index (zero-based) is even
# range(1, 21) creates sequence: index 0 -> 1, index 1 -> 2, index 2 -> 3, etc.
print("Numbers at even indices (index 0, 2, 4...):")
numbers = list(range(1, 21))
for index in range(len(numbers)):
    if index % 2 == 0:
        print(numbers[index], end=" ")
print()
# Exercise 6: While Loop

# Python
while True:
    name = input("Please enter your name: ").strip()
    
    # Check if name is non-numeric (not purely digits) and at least 3 characters long
    if not name.isdigit() and len(name) >= 3 and name.isalpha():
        print("thank you")
        break
    else:
        print("Invalid input. Name must contain letters and be at least 3 characters long.")
# Exercise 7: Favorite Fruits

# Python
# Input favorite fruits
fav_fruits_input = input("Enter your favorite fruits separated by spaces: ")
fav_fruits = fav_fruits_input.split()

# Ask for a single fruit
chosen_fruit = input("Enter the name of any fruit: ").strip()

# Check if chosen fruit is in favorite fruits
if chosen_fruit in fav_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy it!")
# Exercise 8: Pizza Toppings

# Python
toppings = []
base_price = 10.0
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ").strip()
    if topping.lower() == 'quit':
        break
    
    toppings.append(topping)
    print(f"Adding {topping} to your pizza.")

total_cost = base_price + (len(toppings) * topping_price)

print("\n--- Order Summary ---")
print("Your toppings:", ", ".join(toppings) if toppings else "None")
print(f"Total price: ${total_cost:.2f}")
# Exercise 9: Cinemax Tickets & Bonus

# Python
# Main Ticket Calculation
family_size = int(input("How many people are in your family? "))
total_cost = 0

for i in range(family_size):
    age = int(input(f"Enter age for person {i+1}: "))
    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15

print(f"\nTotal ticket cost: ${total_cost}\n")

# Bonus: Restricted Movie Filter
teenagers = ["Alice", "Bob", "Charlie", "David"]
allowed_attendees = []

print("Checking eligibility for restricted movie (ages 16–21)...")
for teen in teenagers:
    age = int(input(f"Enter age for {teen}: "))
    if 16 <= age <= 21:
        allowed_attendees.append(teen)

print("\nFinal list of attendees allowed to watch:", allowed_attendees)