# Exercise 1: Hello World

print("Hello world\n" * 4, end="")

# Exercise 2: Some Math

print((99**3) * 8)

# Exercise 3: What is the output?

5 < 3  # Guess: False
3 == 3  # Guess: True
3 == "3"  # Guess: False (int vs str comparison)
try:
    "3" > 3  # Guess: TypeError (cannot compare str and int using >)
except TypeError:
    pass
"Hello" == "hello"  # Guess: False (case-sensitive)

# Exercise 4: Your computer brand

computer_brand = "Apple"
print(f"I have a {computer_brand} computer.")

# Exercise 5: Your information

name = "Alex"
age = 25
shoe_size = 42
info = f"My name is {name}, I am {age} years old, wear size {shoe_size} shoes, and I love coding!"

print(info)

# Exercise 6: A & B

a = 10
b = 5

if a > b:
    print("Hello World")
# Exercise 7: Odd or Even

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
# Exercise 8: What's your name?

my_name = "Alex"
user_name = input("What is your name? ")

if user_name.strip().title() == my_name:
    print("No way! Are you my evil twin from an alternate dimension?!")
else:
    print(f"Nice to meet you, {user_name}! Sadly, you don't share my awesome name.")
# Exercise 9: Tall enough to ride a roller coaster

height = float(input("Enter your height in cm: "))

if height > 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")