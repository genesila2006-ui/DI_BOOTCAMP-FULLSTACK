# Python
def display_message():
    print("I am learning about functions in Python.")

# Call the function
display_message()
# Exercise 2: What's Your Favorite Book?

# Python
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Call the function
favorite_book("Alice in Wonderland")
# Exercise 3: Some Geography

# Python
def describe_city(city, country="Unknown"):
    print(f"{city} is in {country}.")

# Call with both arguments
describe_city("Reykjavik", "Iceland")

# Call with default country argument
describe_city("Paris")
# Exercise 4: Random

# Python
import random

def compare_numbers(user_number):
    random_number = random.randint(1, 100)
    
    if user_number == random_number:
        print("Success!")
    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")

# Call the function
compare_numbers(50)
# Exercise 5: Let's Create Some Personalized Shirts!

# Python
def make_shirt(size="large", text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size="medium")

# Shirt of any size with a custom message
make_shirt("small", "Custom message")

# Keyword arguments (Bonus)
make_shirt(text="Hello!", size="small")
# Exercise 6: Magicians...

# Python
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    for i in range(len(magicians)):
        magicians[i] = f"{magicians[i]} the Great"

# Modify list and display
make_great(magician_names)
show_magicians(magician_names)
# Exercise 7: Temperature Advice (with Bonuses)

# Python
import random

def get_random_temp(season=None):
    # Step 4 & 5 Bonus: Seasonal ranges with floating-point values
    if season == "winter":
        return round(random.uniform(-10.0, 16.0), 1)
    elif season == "spring" or season == "autumn":
        return round(random.uniform(16.0, 23.0), 1)
    elif season == "summer":
        return round(random.uniform(24.0, 40.0), 1)
    else:
        return round(random.uniform(-10.0, 40.0), 1)

def main():
    # Step 5 Bonus: Month-based season selection
    month = input("Enter a month number (1-12) or press Enter to skip: ").strip()
    
    season = None
    if month.isdigit():
        m = int(month)
        if m in [12, 1, 2]:
            season = "winter"
        elif m in [3, 4, 5]:
            season = "spring"
        elif m in [6, 7, 8]:
            season = "summer"
        elif m in [9, 10, 11]:
            season = "autumn"

    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")

    # Advice conditionals
    if temp < 0:
        print("Brrr, that's freezing! Wear some extra layers today.")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don't forget your coat.")
    elif 16 < temp <= 23:
        print("Nice weather.")
    elif 23 < temp <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It's really hot! Stay cool.")

main()