# Exercise 1: Concatenate lists

# Python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using list.extend() to join without using '+'
list1.extend(list2)
print("Concatenated list:", list1)
# Exercise 2: Range of numbers

# Python
for num in range(1500, 2501):
    # Check if number is divisible by both 5 and 7
    if num % 5 == 0 and num % 7 == 0:
        print(num, end=" ")
print()
# Exercise 3: Check the index

# Python
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

user_name = input("Enter your name: ")

if user_name in names:
    print(names.index(user_name))
else:
    print("Name not found in list.")
# Exercise 4: Greatest Number

# Python
num1 = int(input("Input the 1st number: "))
num2 = int(input("Input the 2nd number: "))
num3 = int(input("Input the 3rd number: "))

greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")
# Exercise 5: The Alphabet

# Python
import string

alphabet = string.ascii_lowercase
vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"'{letter}' is a vowel.")
    else:
        print(f"'{letter}' is a consonant.")
# Exercise 6: Words and letters

# Python
words = []
for i in range(7):
    word = input(f"Enter word {i+1} of 7: ")
    words.append(word)

letter = input("Enter a single letter to look for: ")

for word in words:
    index = word.find(letter)
    if index != -1:
        print(f"The letter '{letter}' first appears at index {index} in '{word}'.")
    else:
        print(f"The letter '{letter}' does not appear in the word '{word}'.")
# Exercise 7: Min, Max, Sum

# Python
numbers = list(range(1, 1000001))

print("Minimum number:", min(numbers))
print("Maximum number:", max(numbers))
print("Sum of numbers:", sum(numbers))
# Exercise 8: List and Tuple

# Python
user_input = input("Enter comma-separated numbers: ")

numbers_list = user_input.split(",")
numbers_tuple = tuple(numbers_list)

print(numbers_list)
print(numbers_tuple)
# Exercise 9: Random number (with Bonuses)

# Python
import random

wins = 0
losses = 0

while True:
    user_guess = input("Guess a number from 1 to 9 (or type 'quit' to exit): ").strip()
    
    if user_guess.lower() == 'quit':
        break
        
    if not user_guess.isdigit() or not (1 <= int(user_guess) <= 9):
        print("Please enter a valid integer between 1 and 9.")
        continue

    secret_number = random.randint(1, 9)
    user_num = int(user_guess)

    if user_num == secret_number:
        print("Winner!")
        wins += 1
    else:
        print(f"Better luck next time. (The number was {secret_number})")
        losses += 1

print("\n--- Game Over ---")
print(f"Total Games Won: {wins}")
print(f"Total Games Lost: {losses}")